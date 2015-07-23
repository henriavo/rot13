#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

form = """

<label>
	<b>Enter some text to ROT13:</b>
	<br>
	<textarea name="text" rows="8" cols="50" >
		%s
	</textarea>
	<br>
	<input type="submit">

	 
</label>

"""

class MainHandler(webapp2.RequestHandler):

	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	def write_form(self, returnText=""):
		self.response.write(form % returnText) 

	def get(self):
		self.write_form()

	def processRot13(self, inputText=""):
		for x in inputText:
			if x.isalpha:
				currentLetter = x.lower()
				if currentLetter in alphabet:
					lowerCase = x.islower()
					if alphabet.index(currentLetter) >= 13:
						rotateIndex = alphabet.index(currentLetter) - 13
						rot13Char = alphabet[rotateIndex]
						if lowerCase:
							finalOutput = finalOutput + rot13Char.lower()
						else:
							finalOutput = finalOutput + rot13Char.upper()

					else:
						rot13Char = alphabet[alphabet.index(currentLetter) + 13]
						if lowerCase:
							finalOutput = finalOutput + rot13Char.lower()
						else:
							finalOutput = finalOutput + rot13Char.upper()
				else:
					finalOutput = finalOutput + x
 	    

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
