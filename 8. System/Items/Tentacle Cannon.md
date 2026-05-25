---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Capacity 5]]", "[[Concussive]]", "[[Fatal d12]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *tentacle cannon* is a *+1 striking* weapon, built using components from squids, krakens, and sometimes even stranger tentacled creatures like alghollthu. It's a distinct type of martial firearm that deals 1d8 piercing damage. It has the capacity 5, concussive, and fatal d12 traits, a range increment of 30 feet, and reload 2. The weapon itself resembles a five-barreled handheld cannon with each barrel made from a hollowed out tentacle.

**Activate—Grasping Deep Shot** `pf2:2` (manipulate)

**Effect** You cause one of the tentacles forming the weapon's five barrels to stretch out and attempt to pull and grab a creature within 15 feet. The tentacle attempts to [[Grapple]] with a +13 bonus. It can attempt to Grapple any creature, regardless of size. On a success, the tentacle pulls the creature up to 10 feet directly towards you, until it's in a square adjacent to you.

**Activate—Unrelenting Grasp** `pf2:1` Interact

**Requirements** The tentacle cannon has a creature [[Grabbed]]

**Effect** You continue to keep the tentacle cannon's hold on one creature it has grabbed. Attempt another check to [[Grapple]] the creature with a +13 bonus.

**Activate—Ink Spray** `pf2:2` Interact

**Frequency** once per hour

**Effect** The cannon fires a spray of ink in a @Template[type:cone|distance:15]. Creatures in the area must attempt a DC 23 [[Reflex]] save. On a failure, the creature is covered in ink and becomes [[Blinded]] for 1 round and [[Dazzled]] for 1 minute or until it removes the ink. On a critical failure, the creature becomes blinded and dazzled; both conditions last for 1 minute or until it removes the ink. The creature, or an adjacent creature, can use an Interact action to remove the ink from its eyes to remove the blinded and dazzled conditions.

**Craft Requirements** The initial raw materials must include the tentacles and ink glands of a creature with a tentacle Strike and ink.

**Source:** `= this.source` (`= this.source-type`)
