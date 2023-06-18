const mapper = {
  "copy": [
    {
      "source": "content",
      "destination": "content_ascii",
      "transformer": (value) => value.replace(/[\W]+/g, ' ').toLowerCase()
    },
  ],
  "rename": [
    {
      "source": "metadata.keywords",
      "destination": "keywords",
    },
    {
      "source": "metadata.description",
      "destination": "description",
    }
  ],
  "remove": [
    {
      "source": "segment",
    }
  ],
};

export default mapper;