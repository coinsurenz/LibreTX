import hashlib
import hmac 
from ecdsa.curves import SECP256k1

class FieldElement:

	def __init__(self, num, prime):
		if num >= prime or num < 0:
			error = 'Num {} not in field range 0 to {}'.format(
				num, prime - 1)
			raise ValueError(error)
		self.num = num
		self.prime = prime

	def __eq__(self, other):
		if other is None:
			return False
		return self.num == other.num and self.prime == other.prime

	def __ne__(self, other):
		# this should be the inverse of the == operator
		return not (self == other)

	def __repr__(self):
		return 'FieldElement_{}({})'.format(self.prime, self.num)

	def __add__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot add two numbers in different Fields')
		num = (self.num + other.num) % self.prime
		prime = self.prime
		return self.__class__(num, prime)

	def __sub__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot add two numbers in different Fields')
		num = (self.num - other.num) % self.prime
		prime = self.prime
		return self.__class__(num, prime)

	def __mul__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot add two numbers in different Fields')
		num = (self.num * other.num) % self.prime
		prime = self.prime
		return self.__class__(num, prime)

	def __pow__(self, n):
		prime = self.prime
		num = pow(self.num, n % (prime - 1), prime)
		return self.__class__(num, prime)

	def __truediv__(self, other):
		if self.prime != other.prime:
			raise TypeError('Cannot add two numbers in different Fields')
		num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
		prime = self.prime
		return self.__class__(num, prime)

	def __rmul__(self, coefficient):
		num = (self.num * coefficient) % self.prime
		return self.__class__(num=num, prime=self.prime)

class Point:

	def __init__(self, x, y, a, b):
		self.a = a
		self.b = b
		self.x = x
		self.y = y
		if self.x is None and self.y is None:
			return
		if self.y**2 != self.x**3 + a * x + b:
			raise ValueError('({}, {}) is not on the curve'.format(self.x, self.y))

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y \
			and self.a == other.a and self.b == other.b

	def __ne__(self, other):
		return not (self == other)

	def __repr__(self):
		if self.x is None:
			return 'Point(infinity)'
		else:
			return 'Point({},{})_{}'.format(self.x.num, self.y.num, self.x.prime)

	def __add__(self, other):
		if self.a != other.a or self.b != other.b:
			raise TypeError('Points {}, {} are not on the same curve'.format(self, other))
		if self.x is None:
			return other
		if other.x is None:
			return self

		if self.x == other.x and self.y != other.y:
			return self.__class__(None, None, self.a, self.b)

		if self.x != other.x:
			s = (other.y - self.y) / (other.x - self.x)
			x = s**2 - self.x - other.x
			y = s * (self.x - x) - self.y
			return self.__class__(x, y, self.a, self.b)

		else:
			s = (3 * self.x**2 + self.a) / (2 * self.y)
			x = s**2 - 2 * self.x
			y = s * (self.x - x) - self.y
			return self.__class__(x, y, self.a, self.b)

	def __rmul__(self, coefficient):
		coef = coefficient
		current = self
		result = self.__class__(None, None, self.a, self.b)
		while coef:
			if coef & 1:
				result += current
			current += current
			coef >>= 1
		return result

A = 0
B = 7
P = 2**256 - 2**32 - 977
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


class S256Field(FieldElement):

	def __init__(self, num, prime=None):
		super().__init__(num=num, prime=P)

	def hex(self):
		return '{:x}'.format(self.num).zfill(64)

	def __repr__(self):
		return self.hex()


class S256Point(Point):

	def __init__(self, x, y, a=None, b=None):
		a, b = S256Field(A), S256Field(B)
		if type(x) == int:
			super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)
		else:
			super().__init__(x=x, y=y, a=a, b=b)

	def __repr__(self):
		if self.x is None:
			return 'S256Point(infinity)'
		else:
			return 'S256Point({},{})'.format(hex(self.x.num), hex(self.y.num))

	def __rmul__(self, coefficient):
		coef = coefficient % N
		return super().__rmul__(coef)

	def sec(self, compressed=True):
		if compressed:
			if self.y.num % 2 == 0:
				return b'\x02' + self.x.num.to_bytes(32, 'big')
			else:
				return b'\x03' + self.x.num.to_bytes(32, 'big')
		else:
			return b'\x04' + self.x.num.to_bytes(32, 'big') + self.y.num.to_bytes(32, 'big')

 
G = S256Point(
	0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
	0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)


class Signature:

	def __init__(self, r, s):
		self.r = r
		self.s = s

	def __repr__(self):
		return 'Signature({:x},{:x})'.format(self.r, self.s)

	def der(self):
		# convert the r part to bytes
		rbin = self.r.to_bytes(32, byteorder='big')
		# if rbin has a high bit, add a 00
		if rbin[0] >= 128:
			rbin = b'\x00' + rbin
		result = bytes([2, len(rbin)]) + rbin
		sbin = self.s.to_bytes(32, byteorder='big')
		# if sbin has a high bit, add a 00
		if sbin[0] >= 128:
			sbin = b'\x00' + sbin
		result += bytes([2, len(sbin)]) + sbin
		return bytes([0x30, len(result)]) + result

	@classmethod
	def parse(cls, signature_bin):
		s = BytesIO(signature_bin)
		compound = s.read(1)[0]
		if compound != 0x30:
			raise RuntimeError("Bad Signature")
		length = s.read(1)[0]
		if length + 2 != len(signature_bin):
			raise RuntimeError("Bad Signature Length")
		marker = s.read(1)[0]
		if marker != 0x02:
			raise RuntimeError("Bad Signature")
		rlength = s.read(1)[0]
		r = int(s.read(rlength).hex(), 16)
		marker = s.read(1)[0]
		if marker != 0x02:
			raise RuntimeError("Bad Signature")
		slength = s.read(1)[0]
		s = int(s.read(slength).hex(), 16)
		if len(signature_bin) != 6 + rlength + slength:
			raise RuntimeError("Signature too long")
		return cls(r, s)

class PrivateKey:

	def __init__(self, secret):
		self.secret = secret
		self.point = secret * G

	def hex(self):
		return '{:x}'.format(self.secret).zfill(64)

	def sign(self, z):
		# we need use deterministic k
		k = self.deterministic_k(z)
		# r is the x coordinate of the resulting point k*G
		r = (k * G).x.num
		# remember 1/k = pow(k, N-2, N)
		k_inv = pow(k, N - 2, N)
		# s = (z+r*secret) / k
		s = (z + r * self.secret) * k_inv % N
		if s > N / 2:
			s = N - s
		# return an instance of Signature:
		# Signature(r, s)
		return Signature(r, s)

	def deterministic_k(self, z):
		k = b'\x00' * 32
		v = b'\x01' * 32
		if z > N:
			z -= N
		z_bytes = z.to_bytes(32, 'big')
		secret_bytes = self.secret.to_bytes(32, 'big')
		s256 = hashlib.sha256
		k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
		v = hmac.new(k, v, s256).digest()
		k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
		v = hmac.new(k, v, s256).digest()
		while True:
			v = hmac.new(k, v, s256).digest()
			candidate = int.from_bytes(v, 'big')
			if candidate >= 1 and candidate < N:
				return candidate
			k = hmac.new(k, v + b'\x00', s256).digest()
			v = hmac.new(k, v, s256).digest()

CURVE_ORDER = SECP256k1.order