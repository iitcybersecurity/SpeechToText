from flask import Response
from flask_restplus import Resource
from Restplus import api


from Endpoints.Utils import JsonTransformer

ns_endpoint = api.namespace('api/storage', description='description')
upload_parser = api.parser()



upload_parser.add_argument("user_id", location='form', type=str)


@ns_endpoint.route("/upload", methods=['POST'])
class apiEndpoint(Resource):

    #Rest Api used to upload a file
    @api.expect(upload_parser)
    def post(self):
	#Prendere il file audio come input
        args = upload_parser.parse_args()
        arg_value = args["user_id"]  # This is FileStorage instance
	audio_input = arg_value
        transformToJson = JsonTransformer()
	#richiamare classificatore 
	#transcription = deepSpeechPrediction(audio_input)
	#result = transcription
	result = arg_value
        jsonResult = transformToJson.transform(result)

        return Response(jsonResult, status=200, mimetype='application/json')

















