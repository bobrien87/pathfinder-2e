---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 200}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your armor responds to your desire to break free of a creature grabbing you by growing spikes.

**Activate** R (attack, concentrate)

**Trigger** You become [[Grabbed]], [[Restrained]], or otherwise held [[Immobilized]] in a creature's grasp, such as by being engulfed or swallowed

**Effect** Your armor suddenly grows spikes, attacking the triggering creature. The armor makes a melee attack with an attack modifier of +14 that deals 2d6 piercing damage. If the creature is swallowing or engulfing you, the attack deals an additional 1d6 untyped damage, and damage from this attack can cut you free if it equals or exceeds the Rupture value of the immobilizing ability. This attack gets an item bonus to the attack roll equal to the armor's item bonus to your AC and an item bonus to damage equal to double that amount.

**Activate** `pf2:1` (attack, concentrate)

**Requirements** You're being held [[Immobilized]] as described in the rune's other activation

**Effect** Your armor attacks the creature immobilizing you. The armor makes a melee attack against the creature, as described in the rune's other activation.

**Source:** `= this.source` (`= this.source-type`)
