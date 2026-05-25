---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 2700}"
usage: "etched-onto-melee-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *spell reservoir* rune creates a pool of eldritch energy within the etched weapon. A spellcaster can spend 1 minute to cast a spell of 3rd rank or lower into the weapon. The spell must require 2 actions or fewer to cast and must be able to target a creature other than the caster. The spell has no immediate effect—it is instead stored for later.

When you wield a *spell reservoir* weapon, you immediately know the name and rank of the stored spell. A *spell reservoir* weapon found as treasure has a 50% chance of having a spell of the GM's choice stored in it.

**Activate—Channeled Release** `pf2:2` (concentrate)

**Requirements** A spell is stored in the weapon

**Effect** Make a Strike with the weapon. You expend the stored spell as part of this Strike; this empties the spell from the weapon and allows a spell to be cast into it again. If the Strike hits, the spell targets the target of the attack. If the spell requires a spell attack roll, the result of your attack roll with the weapon determines the degree of success of the spell, and if the spell requires a saving throw, the DC is 30.

**Activate—Safe Release** A (concentrate)

**Effect** Harmlessly expend the stored spell. This frees the weapon to have a new spell cast into it.

**Source:** `= this.source` (`= this.source-type`)
