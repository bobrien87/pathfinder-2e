---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Enigmatic Conspirant"
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
languages: "Aklo, Common, Elven, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +12, Deception +9, Intimidation +11, Occultism +12, Society +12, Stealth +10, Secret Society Lore +14"
abilityMods: ["+0", "+4", "+0", "+2", "+2", "+3"]
abilities_top:
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Spill Secrets"
    desc: "When the conspiracist critically hits with a Strike, the target must succeed at a DC 21 [[Will]] save or the enigmatic conspiracist perceives the target's surface thoughts for 1 round, as mind reading. This grants the conspiracist a +1 circumstance bonus to AC and saving throws against any creature whose mind they're reading. <br>  <br> > [!danger] Effect: Spill Secrets"
armorclass:
  - name: AC
    desc: "21; **Fort** +8, **Ref** +12, **Will** +12"
health:
  - name: HP
    desc: "60; **Resistances** mental 5"
abilities_mid:
  - name: "Knowing Glance"
    desc: "`pf2:r` **Trigger** The enigmatic conspiracist is targeted by a melee Strike or touch spell <br>  <br> **Effect** With an uncanny look, the enigmatic conspiracist Demoralizes the creature that targeted them. Demoralize loses the auditory trait and gains the visual trait, and the conspiracist doesn't take a penalty if the creature doesn't understand their language. If the Intimidation check critically succeeds, the conspiracist disrupts the triggering action."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +14 (`pf2:1`) (deadly d8, disarm, finesse), **Damage** 1d8+6 piercing plus [[Spill Secrets]]"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Shortbow +14 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6+6 piercing plus [[Spill Secrets]]"
spellcasting: []
abilities_bot:
  - name: "Unbelievable Connection"
    desc: "`pf2:2` The enigmatic conspiracist recites a convoluted conspiracy theory about a creature within 30 feet, then attempts an [[Occultism]] check against the Will DC of that creature. On a success, the target is [[Stupefied 1]] for 1 minute and [[Off Guard]] against the conspiracist's attacks until no longer stupefied. <br>  <br> > [!danger] Effect: Unbelievable Connection"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Powerful organizations work out of public view, shaping lives while facing few consequences. Searching for these secret societies, whether to join them or destroy them, has given the enigmatic conspiracist uncanny insight.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Enigmatic Conspirant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
