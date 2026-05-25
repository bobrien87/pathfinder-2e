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

The *Heart Bloodstone of Arazni* represents protection. While holding the Heart Bloodstone, you can feel the gentle rhythm of a beating heart within the jar.

**Activate—Raise Jar** `pf2:1` (manipulate) You hold the jar aloft, and a nimbus of crimson energy surrounds your body. You gain a +2 circumstance bonus to AC until the start of your next turn.

> [!danger] Effect: Raise Jar

**Activate—Proclaim Resilience** `pf2:2` (concentrate)

**Frequency** once per day

**Requirements** You worship Arazni or are favored by her

**Effect** You make a loud and clear proclamation of your resilience (such as "I will not fall to the hands of my enemies!"). You gain resistance to void damage equal to your level until the beginning of your next turn.

> [!danger] Effect: Proclaim Resilience

**Destruction** The *Heart Bloodstone* turns to dust if a worshipper of Arazni is slain while holding the *Bloodstone* and cursing her name. Any breathing creature within 10 feet of the jar inhales the choking dust, taking 4d6 void damage (DC 28 [[Fortitude]] save). On a failure, the creature also takes 4 persistent,void damage (8 persistent,void damage on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
