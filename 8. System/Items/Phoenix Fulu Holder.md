---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'gp': 2000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elegant wooden frame is decorated with numerous downy red feathers that feel almost uncomfortably hot to the touch. A phoenix fulu holder grants a sort of second "life" to any fulu placed for a time within its frame but also gives the fulu wielder a stylish and eye-catching way of displaying such a treasure. You can place any fulu into a phoenix fulu holder as an Interact action.

**Activate—Duplicate Fulu** `pf2:1` (manipulate)

**Frequency** once per day

**Requirements** An 11th- or lower-level fulu is stored in the phoenix fulu holder

**Effect** You take the fulu from the phoenix fulu holder, and an instant later, a glowing image of the fulu you removed manifests in the frame. If the previously stored fulu is consumed within the next 24 hours, the flickering image within the phoenix fulu holder becomes a solid and fully functional duplicate of that fulu. This duplicated fulu functions identically to the original fulu, but if not affixed within 24 hours of its formation, it fades away and vanishes. A duplicated fulu can't be placed in a phoenix fulu holder to be further duplicated.

**Source:** `= this.source` (`= this.source-type`)
