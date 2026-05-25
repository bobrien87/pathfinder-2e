---
type: creature
group: ["Dragon", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zombie Dragon"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Dragon"
trait_02: "Mindless"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: "Zombie"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +19"
abilityMods: ["+6", "+3", "+4", "-5", "+3", "-2"]
abilities_top:
  - name: "Slow"
    desc: "The zombie dragon is permanently [[Slowed]] 1 and can't use reactions."
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +18, **Will** +16"
health:
  - name: HP
    desc: "210; void healing; **Immunities** bleed, death effects, disease, mental, paralyzed, poison, unconscious; **Weaknesses** slashing 10, vitality 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Upper Jaw +21 (`pf2:1`) (reach 15 ft.), **Damage** 2d10+12 piercing"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, reach 10 ft.), **Damage** 2d8+12 slashing"
  - name: "Melee strike"
    desc: "Tail +19 (`pf2:1`) (reach 20 ft.), **Damage** 2d6+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Viscera Breath"
    desc: "`pf2:2` The zombie dragon breathes a wave of fetid viscera that deals @Damage[5d6[bludgeoning],5d6[poison]|options:area-damage]{5d6 bludgeoning damage and 5d6 poison damage} (DC 28 [[Reflex]] save). A creature that critically fails is also [[Sickened]] 2. The zombie dragon can't use Viscera Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The rotted husk of a once great dragon, this abomination has lost all its former splendor, but none of the ferocity. Its patchy, rotted wings don't generate enough lift to keep it aloft, but the foul necromantic energies animating it still allow it to fly, albeit slowly.

Necromancers most often create these mindless undead as obedient, expendable servitors. Left to its own devices, a zombie seeks only to consume the living, stopping only when its rotting body can no longer hold together.

```statblock
creature: "Zombie Dragon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
