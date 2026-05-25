---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "False Priest"
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
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +8, Deception +12, Performance +12, Religion +8, Society +6"
abilityMods: ["+0", "+4", "+3", "+0", "+2", "+4"]
abilities_top:
  - name: "Deceiver's Surprise"
    desc: "On the first round of combat, if the false priest rolls Deception or Performance for initiative, creatures that haven't acted yet are [[Off Guard]] to the false priest."
  - name: "Sneak Attack"
    desc: "The false priest deals an extra 1d6 precision damage to [[Off Guard]] creatures. This increases to 2d6 precision damage against creatures off-guard due to the false priest's [[Feint]] or deceiver's surprise."
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "50"
abilities_mid:
  - name: "The Jig Is Up"
    desc: "`pf2:r` **Frequency** once per hour <br>  <br> **Trigger** The false priest critically fails a Deception or Performance check <br>  <br> **Effect** The false priest Strides."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +12 (`pf2:1`) (deadly d8, disarm, finesse), **Damage** 1d6+8 piercing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +12 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Fickle Prophecy"
    desc: "`pf2:1` The false priest convinces someone of their omnipotence by attempting a [[Deception]] check compared to the creature's Will DC. <br>  <br> If successful, the target gains 1d8+4 temporary Hit Points that last for 1 hour or until the false priest removes them by rebuking the target, whichever occurs first. <br>  <br> > [!danger] Effect: Fickle Prophecy"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Belief is perhaps the strongest force in the universe. Instilling belief only to use it against someone in deceit, however, is the purview of a false priest.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "False Priest"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
