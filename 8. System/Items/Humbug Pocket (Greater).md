---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Occult]]"]
price: "{'gp': 12500}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Fine silk lines this fashionable pocket, which is typically cinched to a belt or tailored into a piece of formal clothing. The pocket can hold no more than one item of light Bulk, plus incidental items of negligible Bulk. The pocket grants you a +3 item bonus to Society and to Stealth checks to [[Conceal an Object]] in the pocket.

The pocket can produce stationery and writing implements of high quality. When you [[Create a Forgery]], you can use the pocket to produce ideal materials to make the forgery. Any materials must be able to fit through the opening of the pocket, such as a roll of parchment, an inkwell, or a loupe. Though they're excellent tools, they don't have any value if sold and disappear once their function in making a forgery is fulfilled.

**Activate—Papers Please** `pf2:1` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You create up to 5 temporary forgeries by imagining the documents you need and pulling them from the pocket. Attempt to Create a Forgery of the documents you desire, with the GM rolling the secret check as normal. Their quality is based on your check, but the documents disintegrate after 1 hour.

All 5 forgeries must serve a similar purpose—five invitations to the same party for different attendees, for example. Attempt only one check for all the documents.

**Source:** `= this.source` (`= this.source-type`)
