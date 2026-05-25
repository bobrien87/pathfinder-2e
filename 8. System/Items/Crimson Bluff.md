---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Agile]]", "[[Finesse]]", "[[Illusion]]", "[[Magical]]", "[[Twin]]"]
price: "{'gp': 6500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking grievous sawtooth saber* has a red hilt and a purple-black blade. Favored by Red Mantis assassins who enjoy using illusions to confound their targets, a *crimson bluff* constantly flickers and flashes, creating brief afterimages that can be quite distracting. If you use a *crimson bluff* as part of a gesture when you [[Create a Diversion]], you gain a +2 item bonus to your Deception check.

**Activate—Shimmer Step** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast [[Blur]] and then you Step or Stride.

**Activate—Swap Places** `pf2:r` (concentrate)

**Frequency** once per day

**Requirements** You are under the effects of *blur*

**Trigger** An enemy would hit you with a melee Strike

**Effect** You swiftly dodge to the side as a momentary image of yourself manifests to distract the foe. The triggering Strike uses the outcome for one degree of success worse than the result of the attack roll. The duration of your *blur* effect is reduced by 2 rounds.

**Source:** `= this.source` (`= this.source-type`)
