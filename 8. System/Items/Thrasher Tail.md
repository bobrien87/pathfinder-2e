---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Clockwork]]", "[[Kobold]]", "[[Mechanical]]"]
price: "{'gp': 620}"
usage: "worn"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Kobolds admire well-designed objects, especially if it gives them an opportunity to pack it with traps and surprises. This prosthetic tail hides numerous blades and spikes, tensioned and wound around a spring-loaded trigger at the base of the prosthesis. Resetting and reattaching a sprung thrasher tail takes 10 minutes.

**Activate** R

**Trigger** You're [[Grabbed]]

**Effect** Your tail comes off in your opponent's hand, and the mechanism unwinds, causing the blades and spikes to protrude and the tail to spin and thrash. The tail deals 8d6 slashing damage to the opponent who has you grabbed with a DC 25 [[Reflex]] save. Regardless of the result of their save, you're no longer grabbed.

**Source:** `= this.source` (`= this.source-type`)
