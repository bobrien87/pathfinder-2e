---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Artifact]]", "[[Divine]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The *Spleen Bloodstone of Arazni* represents freedom. Holding the *Spleen Bloodstone* makes you feel as if no bonds can contain you.

**Activate—Sure Footing** `pf2:1` to `pf2:3` (concentrate)

**Requirements** You aren't [[Immobilized]]

**Frequency** once per hour

**Effect** You Step or Stride, treating both difficult and greater difficult terrain as normal terrain during the movement. For each additional action you spend, you can Step or Stride again with the same benefits. If you have a climb or fly Speed, you can instead Climb or Fly respectively.

**Activate—Break Bonds** `pf2:f` (concentrate)

**Requirements** You worship Arazni or are favored by her

**Frequency** once per day

**Effect** The [[Confused]], [[Controlled]], [[Grabbed]], [[Immobilized]], [[Paralyzed]], [[Petrified]], and [[Restrained]] conditions, as well as any Speed penalties affecting you, immediately end unless the effect is magical and of 12th level or higher. You can use this ability even if your actions are restricted or otherwise decided for you (such as being confused or controlled).

**Destruction** If a worshipper of Arazni willingly gains the controlled condition or becomes undead while holding the *Spleen Bloodstone*, the *Bloodstone* explodes, dealing 10d6 force damage to all creatures in a @Template[type:emanation|distance:20] (DC 28 [[Reflex]] save).

**Source:** `= this.source` (`= this.source-type`)
