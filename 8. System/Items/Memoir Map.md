---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 13}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your journeys and the major events in your life that occur after you obtain this tattoo appear on it, your life story traced upon your skin. Each time you journey somewhere new or accomplish something noteworthy to you, a design or symbol appears, representing the event. The positions of these images are relative in location, but measurements aren't exact. A memoir map starts with an icon representing your location when you receive the tattoo, usually over the heart, and grows from there. Traveling to another plane causes a new portion to appear on a different part of your body to represent that plane. If you want a record of your life before you receive your memoir map, you can have the tattoo artist embellish the map to represent past events.

**Source:** `= this.source` (`= this.source-type`)
