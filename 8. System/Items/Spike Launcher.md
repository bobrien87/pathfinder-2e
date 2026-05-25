---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Backstabber]]", "[[Fatal aim d12]]", "[[Kickback]]"]
price: "{'gp': 250}"
usage: "held-in-one-plus-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Built from the spiked tail of a manticore, a *spike launcher* is designed to launch large, spear-like projectiles. A *spike launcher* is a *+1 striking* weapon. It's a distinct type of martial firearm that deals 1d8 piercing damage. It has the backstabber, fatal aim d12, and kickback traits with a range increment of 120 feet and reload 2. It uses the critical specialization of the bow weapon group, rather than the firearm critical specialization.

**Activate—Spike Shot** `pf2:3` (manipulate)

**Frequency** once per day

**Requirements** The *spike launcher* is loaded

**Effect** The *spike launcher* fires a volley of spikes in a @Template[type:burst|distance:10] centered anywhere within its range. Make a Strike with the *spike launcher* against each creature in the area; your multiple attack penalty does not increase until after you have resolved all these attacks. On a success, the spike causes the creature to take a –5-foot status penalty to their Speed. On a critical success, the creature becomes [[Immobilized]] instead. In either case, the creature, or an adjacent creature, can use an Interact action to remove the spike and end the penalty or immobilized condition.

**Craft Requirements** The initial raw materials must include the tail of a manticore.

**Source:** `= this.source` (`= this.source-type`)
