---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 600}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tiny silver hooks decorate these fine silk gloves. They grant a +2 item bonus to Thievery and allow you to cast [[Telekinetic Hand]] as an innate occult spell.

If you are also wearing a *charlatan's cape*, whenever you would move an object using *telekinetic hand*, you may instead have it disappear in a puff of smoke and reappear hovering in a space adjacent to yours. This is a teleportation effect. The item hovers until the end of your turn or until retrieved with an Interact action.

**Source:** `= this.source` (`= this.source-type`)
