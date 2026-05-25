---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gang Leader"
level: "7"
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
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +17, Deception +15, Intimidation +17, Society +11, Stealth +17, Thievery +15, Underworld Lore +15"
abilityMods: ["+4", "+4", "+2", "+2", "-1", "+4"]
abilities_top:
  - name: "Gang Up"
    desc: "Any enemy is [[Off Guard]] against the gang leader's melee attacks due to flanking as long as the enemy is within melee reach of both the gang leader and one of the gang leader's allies."
  - name: "Sneak Attack"
    desc: "The gang leader deals an extra 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "24; **Fort** +13, **Ref** +17, **Will** +12"
health:
  - name: HP
    desc: "110"
abilities_mid:
  - name: "Deny Advantage"
    desc: "The gang leader isn't [[Off Guard]] to creatures of 7th level or lower that are [[Hidden]], [[Undetected]], flanking, or using surprise attack."
  - name: "Evasive Reflexes"
    desc: "When the gang leader rolls a success on a Reflex save, they get a critical success instead."
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** The gang leader is targeted with an attack by an attacker they can see <br>  <br> **Effect** The gang leader gains a +2 circumstance bonus to AC against the triggering attack."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted are [[Off Guard]] to the gang leader."
  - name: "Brutal Rally"
    desc: "`pf2:r` **Trigger** The gang leader rolls a critical hit against a creature <br>  <br> **Effect** All allies that can see the gang leader gain a +1 circumstance bonus to attack rolls until the start of the gang leader's next turn. <br>  <br> > [!danger] Effect: Brutal Rally"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +18 (`pf2:1`) (agile, magical, versatile s), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +17 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Quick Draw"
    desc: "`pf2:1` The gang leader Interacts to draw a weapon, then Strikes with that weapon."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Gang leaders direct cutthroats, killers, thieves, and toughs. The gang leader often appears alongside a bandit gang or other criminals.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Gang Leader"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
