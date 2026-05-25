---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Occult]]"]
price: "{'gp': 650}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Fine silk lines this fashionable pocket, which is typically cinched to a belt or tailored into a piece of formal clothing. The pocket can hold no more than one item of light Bulk, plus incidental items of negligible Bulk. The pocket grants you a +2 item bonus to Society and to Stealth checks to [[Conceal an Object]] in the pocket.

The pocket can produce stationery and writing implements of high quality. When you [[Create a Forgery]], you can use the pocket to produce ideal materials to make the forgery. Any materials must be able to fit through the opening of the pocket, such as a roll of parchment, an inkwell, or a loupe. Though they're excellent tools, they don't have any value if sold and disappear once their function in making a forgery is fulfilled.

**Activate—Papers Please** `pf2:1` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You create a temporary forgery by imagining the document you need and pulling it from the pocket. Attempt to Create a Forgery of the document you desire, with the GM rolling the secret check as normal. Its quality is based on your check, but the document disintegrates after 1 hour.

**Source:** `= this.source` (`= this.source-type`)
