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
<form method ="post">

	<label>
		<b>Enter some text to ROT13:</b>
		<br>
		<textarea name="text" rows="8" cols="50" >
			%s
		</textarea>
		<br>
		<br>
		<input type="submit">

		 
	</label>
</form>

"""

class MainHandler(webapp2.RequestHandler):

	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	def write_form(self, returnText=""):
		self.response.write(form % returnText) 

	def get(self):
		self.write_form()

	def post(self):
		inputText = self.request.get('text')
		rot13Text = self.processRot13(inputText)
		self.write_form(rot13Text)


	def processRot13(self, inputText=""):
		finalOutput = ""
		for x in inputText:
			if x.isalpha:
				currentLetter = x.lower()
				if currentLetter in self.alphabet:
					lowerCase = x.islower()
					if self.alphabet.index(currentLetter) >= 13:
						rotateIndex = self.alphabet.index(currentLetter) - 13
						rot13Char = self.alphabet[rotateIndex]
						if lowerCase:
							finalOutput = finalOutput + rot13Char.lower()
						else:
							finalOutput = finalOutput + rot13Char.upper()

					else:
						rot13Char = self.alphabet[self.alphabet.index(currentLetter) + 13]
						if lowerCase:
							finalOutput = finalOutput + rot13Char.lower()
						else:
							finalOutput = finalOutput + rot13Char.upper()
				else:
					finalOutput = finalOutput + x

		return finalOutput
 	    

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
