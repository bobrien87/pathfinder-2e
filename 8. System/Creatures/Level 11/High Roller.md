---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "High Roller"
level: "11"
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
    desc: "+22"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +24, Intimidation +22, Society +21, Thievery +22, Games Lore +26"
abilityMods: ["+1", "+5", "+0", "+2", "+3", "+5"]
abilities_top:
  - name: "Gaming Arsenal"
    desc: "The high roller treats all game tools—such as cards (used in the stat block's Strike entries), dice, coins, and gambling tokens—as melee weapons with a d4 damage die and the agile, finesse and thrown 20 feet traits. The high roller gets a +1 item bonus to attack rolls with them and deals two damage dice. The damage type depends on the item and is determined by the GM."
armorclass:
  - name: AC
    desc: "30; **Fort** +17, **Ref** +24, **Will** +22"
health:
  - name: HP
    desc: "150"
abilities_mid:
  - name: "+4 to Sense Motive"
    desc: ""
  - name: "Tip the Scales"
    desc: "`pf2:r` **Trigger** A creature the high roller is observing critically fails a check <br>  <br> **Effect** The high roller picks up on luck that others dropped. They roll twice on their next d20 roll before the end of their next turn and take the better result."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +23 (`pf2:1`) (deadly d8, disarm, finesse, magical), **Damage** 2d6+11 piercing"
  - name: "Melee strike"
    desc: "Fist +22 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning"
  - name: "Melee strike"
    desc: "Card +23 (`pf2:1`) (agile, finesse), **Damage** 2d4+11 slashing"
  - name: "Melee strike"
    desc: "Card +23 (`pf2:1`) (agile, thrown 20), **Damage** 2d4+11 slashing"
spellcasting: []
abilities_bot:
  - name: "Lucky Momentum"
    desc: "`pf2:1` **Requirements** The high roller's last action was a critical success <br>  <br> **Effect** The high roller either Strides twice or attempts a Strike that deals an additional 4d6 precision damage and deals half damage on a failure (but not a critical failure)."
  - name: "Royal Flush Flurry"
    desc: "`pf2:2` **Frequency** once per hour <br>  <br> **Requirements** The high roller has at least 16 cards in one hand <br>  <br> **Effect** The high roller unleashes the cards in a @Template[type:cone|distance:30], dealing @Damage[16d4[slashing]|options:area-damage] damage to all creatures in the area with a DC 30 [[Reflex]] save. This ability expends the full deck of cards held."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Those with a particular mastery over luck can make a living through games of chance as professional gamblers.

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "High Roller"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
