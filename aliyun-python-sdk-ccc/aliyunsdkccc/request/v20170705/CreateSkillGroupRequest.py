# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateSkillGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'CreateSkillGroup','ccc')

	def get_SkillLevels(self):
		return self.get_query_params().get('SkillLevels')

	def set_SkillLevels(self,SkillLevels):
		for i in range(len(SkillLevels)):	
			if SkillLevels[i] is not None:
				self.add_query_param('SkillLevel.' + str(i + 1) , SkillLevels[i]);

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_OutboundPhoneNumberIds(self):
		return self.get_query_params().get('OutboundPhoneNumberIds')

	def set_OutboundPhoneNumberIds(self,OutboundPhoneNumberIds):
		for i in range(len(OutboundPhoneNumberIds)):	
			if OutboundPhoneNumberIds[i] is not None:
				self.add_query_param('OutboundPhoneNumberId.' + str(i + 1) , OutboundPhoneNumberIds[i]);

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_UserIds(self):
		return self.get_query_params().get('UserIds')

	def set_UserIds(self,UserIds):
		for i in range(len(UserIds)):	
			if UserIds[i] is not None:
				self.add_query_param('UserId.' + str(i + 1) , UserIds[i]);