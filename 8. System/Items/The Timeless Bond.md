---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You've linked your lifespan to your bound dragon. Your natural physical aging ceases and you gain the Draconic Vitality action, but your soul grows withered and scabrous by the weight of a dragon's experience with time.

Once per week, from any distance, the dragon can use a free action, which has the concentrate trait, to become [[Quickened]] for 1 minute. They can use the extra action to Stride, Strike, or to contribute an action to casting a spell. When the dragon uses this ability, you age 10 years and become [[Drained]] 3 for 1 hour.

**Draconic Vitality** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** Reduce your doomed value by 2. For 1 hour, you gain a +2 status bonus to saves against poisons and diseases, and a status bonus equal to your level to Hit Points you regain from spells with the same tradition as your bound dragon.

**Oathbreaker's Calamity** Should either party break the oath, you begin aging at an accelerated rate. Every 1d6 days, you must succeed at a flat DC 14 check or age 10 years and become [[Drained]] 3. In turn, the dragon loses years of experience, reducing its age 100 years every time you fail the flat check. If the dragon is de-aged past the time they made the pact, the pact remains, but the dragon loses all memories of you and the pact.

**Source:** `= this.source` (`= this.source-type`)
