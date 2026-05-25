---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Mythic]]"]
cast: "`pf2:2`"
area: "10-foot emanation"
duration: "1 minute"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Magic surges to life around you, feeding on the raw power you radiate. Choose one of the following abilities to affect creatures in your aura. You can choose a different effect, ending the previous one, by Sustaining the spell. You can Dismiss the aura.

- **Interference** The excess magic surrounding you creates a mental static. All saving throws against mental effects gain a +2 circumstance bonus.
- **Mana Well** You become a source of pure magic that allows spells to be cast more freely. Allied creatures that would normally be required to attempt a flat check to Cast a Spell (such as from the [[Stupefied]] condition) automatically succeed.
- **Overpower Resistance** Surging magic penetrates most defenses. Any time a spell affects a creature within the aura, that spell ignores an amount of the creature's resistance equal to your level. This applies to all damage the spell deals, including persistent damage and damage caused by an ongoing effect of the spell. This doesn't cause the spell to ignore immunities.
- **Ward** Stray magical energy diffuses damaging spells. Any time a spell affects a creature within the aura, the damage dealt by the spell is reduced by an amount equal to your level. This applies to all damage the spell deals, including persistent damage and damage caused by an ongoing effect of the spell.

**Source:** `= this.source` (`= this.source-type`)
