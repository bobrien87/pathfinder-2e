---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Cursed]]", "[[Extradimensional]]", "[[Magical]]"]
price: "{'gp': 6000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item appears to be and functions as a portable hole, but it's actually the maw of an alien extradimensional creature akin to and older than a *bag of devouring*. Any animal or vegetable matter put in the hole has a chance of triggering the creature's interest. Whenever you reach into the hole to retrieve an item or place an animal or plant product within the bag, roll a DC 11 flat check. On a success, the hole ignores the intrusion. On a failure, the *mother maw* devours the triggering material, removing it from existence. The maw can't eat artifacts. If the triggering material isn't entirely inside the maw, such as when someone reaches inside, the *mother maw* attempts to pull it completely inside using a [[Grapple]] action with a +28 Athletics bonus. On a success, it devours the victim or object.

Whenever the maw critically fails the Athletics check, it regurgitates one creature or object it previously devoured. The condition of the vomited creature or object depends on its resilience and the time it has spent inside the maw. Typically, the maw spews forth items it finds difficult to digest, such as those made of adamantine or protected by magic. It can and does regurgitate remains, though.

**Source:** `= this.source` (`= this.source-type`)
