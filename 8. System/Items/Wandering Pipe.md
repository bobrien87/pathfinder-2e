---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Artifact]]", "[[Invested]]", "[[Magical]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This long-stemmed pipe always emits a thin plume of smoke, even when not lit or in active use. The exact material the pipe is made of varies in every accounting; sometimes made of polished oak, other times ebony, sometimes stone, and in one Erutaki legend the pipe is made of pure ice that somehow holds a flame. Though the *wandering pipe* is not intelligent, it is rumored to possess a certain capriciousness, leaving the possession of mortals whose lives are not exciting enough but inevitably finding its way back to its one true owner.

When held in one hand, the pipe grants its holder a +2 circumstance bonus to Deception checks but imposes a -1 circumstance penalty to Stealth checks made to Hide or [[Sneak]], as its telltale plume of smoke gives away the bearer's position.

**Activate—Smoky Protections** `pf2:2` (concentrate, manipulate, primal)

**Frequency** once per hour; **Cost** 1 Mythic Point

**Effect** For the next 10 minutes, smoke gathers around you buoying your steps and protecting you. For the duration of this effect, you gain a fly Speed equal to your land Speed and automatically hover in place, and you have concealment from ranged attacks.

> [!danger] Effect: Smoky Protections

**Destruction** The *wandering pipe* can be broken as easily as any other wooden pipe, but it always reforms afterward in the hands of the Immortal Trickster or one of his bonded mortals. It can only be broken by the hands of one of the Trickster's bonded mortals who is an honest person acting with good intent; it is said that if this occurs, the Trickster would also be significantly weakened as a result.

**Source:** `= this.source` (`= this.source-type`)
