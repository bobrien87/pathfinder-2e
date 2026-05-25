---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Flexible]]", "[[Invested]]", "[[Magical]]", "[[Noisy]]"]
price: "{'gp': 360}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 silver chain shirt* has a collar adorned with stitched images of the phases of the moon. You can see in moonlight as though you had low-light vision.

**Activate—Dim Sight** A (manipulate)

**Frequency** one per day

**Effect** You touch the stitched image of the new moon on the armor's collar and suppress the [[Dazzled]] condition for 1 minute.

**Craft Requirements** The initial raw materials must include 33 gp of silver.

**Source:** `= this.source` (`= this.source-type`)
