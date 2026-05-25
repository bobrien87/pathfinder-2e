---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Combination]]", "[[Concussive]]", "[[Fatal d8]]", "[[Magical]]"]
price: "{'gp': 230}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Ritually constructed from the bones of a nightmare, a *nightmare's lament* is a *+1 striking rapier pistol*. Thin wisps of dark smoke continually surround the red-flecked blade.

**Activate—Fuming Cloak** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** For 1 minute, the *nightmare's lament* continually vents thick, black smoke that creates concealment in a 15-foot aura around the gun's wielder. The wielder of the *nightmare's lament* can see through this smoke. A creature that begins its turn in the area becomes [[Sickened]] 2 (DC 23 [[Fortitude]] save negates) and is then temporarily immune to the sickness from the smoke for 1 minute. The wielder of the *nightmare's lament*, any creature currently holding its breath (or that does not need to breathe), and any creature immune to poison are immune to the aura's sickened effect but not the concealment.

> [!danger] Effect: Aura: Fuming Cloak

**Craft Requirements** The initial raw materials must include the rib bones and inner fire of a nightmare.

**Source:** `= this.source` (`= this.source-type`)
