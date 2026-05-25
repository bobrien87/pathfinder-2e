---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mastermind"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Common (two additional languages)"
skills:
  - name: Skills
    desc: "Arcana +13, Deception +15, Diplomacy +15, Intimidation +15, Occultism +15, Performance +17, Religion +11, Society +17, Stealth +11, Thievery +9, Underworld Lore +17"
abilityMods: ["+0", "+3", "+0", "+4", "+2", "+4"]
abilities_top:
  - name: "+7 to Sense Motive"
    desc: ""
  - name: "Manipulation Specialist"
    desc: "When competing in a social or intellectual arena, the mastermind is a 7th-level challenge."
  - name: "Versatile Performance"
    desc: "The mastermind can use Performance instead of Diplomacy to `act make-an-impression skill=performance` and instead of Deception to `act impersonate skill=performance`."
  - name: "Scoundrel's Feint"
    desc: "When the mastermind successfully Feints, the target is [[Off Guard]] against the mastermind's melee attacks until the end of the mastermind's next turn. On a critical success, the target is off-guard against all melee attacks for that time, not just the mastermind's."
  - name: "Sneak Attack"
    desc: "The mastermind deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "20; **Fort** +6, **Ref** +11, **Will** +16"
health:
  - name: HP
    desc: "55"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +13 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +13 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+6 piercing"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14<br>**2nd** (3 slots) [[Blur]], [[Invisibility]], [[Paranoia]]<br>**1st** (3 slots) [[Charm]], [[Charm]], [[Daze]], [[Detect Magic]], [[Illusory Disguise]], [[Illusory Object]], [[Message]], [[Prestidigitation]], [[Sigil]]"
  - name: "Bard Composition Spells"
    desc: "DC 22, attack +14<br>**1st** [[Courageous Anthem]], [[Uplifting Overture]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Masterminds weave long-ranged plots to see their nefarious goals come to fruition, deftly manipulating those around them, turning enemies into friends and then pitting them against one another.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Mastermind"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
