---
type: creature
group: ["Mindless", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Flaming Skull"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +7"
abilityMods: ["+1", "+4", "+1", "-5", "+3", "+0"]
abilities_top:
  - name: "Flaming Shroud"
    desc: "A flaming skull is shrouded in hideous flames. It deals 1d6 fire damage to any unattended item it touches and on a forehead Strike. On a critical hit with a Strike, the target catches fire, taking 1d4 persistent,fire."
armorclass:
  - name: AC
    desc: "18; **Fort** +5, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "30; void healing; **Immunities** bleed, death effects, disease, fire, paralyzed, poison, unconscious; **Weaknesses** vitality 3"
abilities_mid:
  - name: "Fiery Explosion"
    desc: "When destroyed, a flaming skull explodes in a blast of fire and bone that deals @Damage[1d6[piercing],1d6[fire]]{1d6 piercing damage plus 1d6 fire damage} to each adjacent creature (DC 18 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Forehead +10 (`pf2:1`) (finesse), **Damage** 1d6+3 bludgeoning plus 1d6 fire"
  - name: "Ranged strike"
    desc: "Spitfire +10 (`pf2:1`) (agile, fire), **Damage** 1d12+2 fire"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

More dangerous than simple severed heads, these skulls are wreathed in unearthly flames.

Beheaded are the reanimated heads of decapitation victims. These mindless undead fly through the air or roll around to attack their prey.

```statblock
creature: "Flaming Skull"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
