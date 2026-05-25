---
type: creature
group: ["Incorporeal", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Banshee"
level: "17"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Spirit"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Darkvision]]"
languages: "Common, Elven"
skills:
  - name: Skills
    desc: "Acrobatics +31, Intimidation +32, Occultism +25"
abilityMods: ["-5", "+6", "+2", "+0", "+7", "+7"]
abilities_top:
  - name: "Hears Heartbeats"
    desc: "The banshee can hear heartbeats within 60 feet of it as an imprecise sense."
  - name: "Sunlight Powerlessness"
    desc: "A banshee in sunlight is [[Clumsy]] 2 and [[Stunned]] 2."
  - name: "Terrifying Touch"
    desc: "A creature damaged by the banshee's touch that isn't already frightened must attempt a DC 38 [[Will]] save (DC 43 [[Will]] save if the attack was a critical hit). If the creature fails its save, it's [[Frightened]] 2; on a critical failure, the creature also cowers with fear and is [[Stunned]] 4. If the creature is protected against fear by a spell or magic item, the banshee's touch first attempts to counteract the protection effect, with the effect of a 9th-rank [[Dispel Magic]] spell."
armorclass:
  - name: AC
    desc: "39; **Fort** +25, **Ref** +29, **Will** +32"
health:
  - name: HP
    desc: "250; void healing; **Immunities** bleed, death effects, disease, paralyzed, paralyzed, poison, precision, unconscious; **Resistances** all damage 12 except force, ghost touch, spirit, vitality"
abilities_mid:
  - name: "Spectral Ripple"
    desc: "When a banshee Strides at least 10 feet, they're [[Concealed]] until the start of their next turn."
  - name: "Vengeful Spite"
    desc: "`pf2:r` **Trigger** A foe critically hits the banshee, or the banshee critically fails their save against a foe's damaging effect <br>  <br> **Effect** The banshee lashes back at their tormentor, dealing @Damage[(4d10+14)[mental]] damage with a DC 38 [[Will]] save and applying the effects of terrifying touch based on the results of the same Will save."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hand +32 (`pf2:1`) (finesse, magical), **Damage** 4d10+14 void plus [[Terrifying Touch]]"
spellcasting: []
abilities_bot:
  - name: "Wail"
    desc: "`pf2:2` The banshee unleashes a soul-chilling [[Wails of the Damned]] (DC 38 [[Fortitude]] save, 8d10 void). This Wail overcomes silence and similar effects of 5th rank or lower. The banshee can instead use Wail as a three-action activity to overcome such effects of up to 8th rank. <br>  <br> The banshee's Wail resonates for 1 round, and any creature that comes within the area during that time must attempt a save against the effect. A creature can't be affected more than once by the same Wail. The banshee can't Wail again for `gmr 1d4 #Recharge Wail` rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Banshees are the furious, tormented souls of those bound to the world by a betrayal that defined the final hours of their lives. Some banshees arise from those who were slain by trusted friends and allies, or whose loved ones betrayed them on their deathbeds. Others spawn from those whose treacherous deeds shortly before their deaths left a stain upon their souls. Regardless of their origin, banshees despise the living. This hatred of life is all too often a horrific inversion of their personalities in life. Some speculate that the more kind-hearted the person (and the more wrenching the betrayal), the crueler the banshee.

Banshees rarely stray far from where they perished and typically haunt thick forests and canopied swamps where little light graces the ground. Many banshees are elves and can be found in the elven nation of Kyonin, specifically in Tanglebriar, the sinister domain of the demon Treerazer. Similarly, a large number of banshees can be found lurking in the frozen wastes in northern Avistan, created from a cruel and widespread betrayal that is centuries old.

```statblock
creature: "Banshee"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
