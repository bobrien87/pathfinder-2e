---
type: item
source-type: "Remaster"
level: "25"
traits: ["[[Agile]]", "[[Artifact]]", "[[Divine]]", "[[Thrown 20]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ordinary-looking silver tankard functions as a *+4 major striking returning shockwave light hammer* when wielded as a weapon. Imbued with Cayden Cailean's courage, you are immune to fear effects. Any liquid poured into the tankard transforms into a strong, alcoholic ambrosia that remains contained safely within until you drink it. Drinking the ambrosia Activates the tankard, with one of the following effects. If you aren't the one blessed to borrow the tankard, you are [[Drained]] 4 and [[Enfeebled]] 4 while holding it, and its magic doesn't function for you.

**Activate** R (manipulate)

**Trigger** You are targeted or included in the area of a fear effect

**Effect** Calmly swigging a drink on the battlefield turns your foe's attempt to frighten you against them. The fear effect is counteracted for all targets, and the creature that created the effect must attempt a saving throw as if it alone were the original target of the effect.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You drink from the tankard, ending the controlled, [[Grabbed]], [[Immobilized]], [[Paralyzed]], [[Restrained]], and slowed conditions on yourself and creatures of your choice within 120 feet of you, as well as anything giving such targets a circumstance penalty to Speed. Any effect causing these conditions ends, and if the source of the effect is an item, that item can't produce the effect for 1 week, provided it is of a level lower than the tankard's. If a target needs to [[Escape]] an effect imposing any of these conditions, it automatically does so on its next attempt. You can Activate this ability even if one of the listed conditions would normally prevent you from doing so (such as paralyzed).

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You enhance yourself with a shard of Cayden's divine fortune and cast indestructibility.

**Destruction** If an unholy creature carries Cayden's Tankard into the Starstone Cathedral, drinks from it, and returns outside with it, the tankard shatters.

**Source:** `= this.source` (`= this.source-type`)
