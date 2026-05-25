---
type: creature
group: ["Air", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cloud Giant"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Air"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Jotun, Sussuran"
skills:
  - name: Skills
    desc: "Athletics +26, Crafting +21, Diplomacy +24, Intimidation +26, Performance +21"
abilityMods: ["+7", "+0", "+5", "+1", "+3", "+1"]
abilities_top:
  - name: "Cloudsight"
    desc: "Cloud giants ignore concealment from weather conditions, including clouds and rain."
armorclass:
  - name: AC
    desc: "30; **Fort** +25, **Ref** +18, **Will** +21"
health:
  - name: HP
    desc: "220"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ranseur +25 (`pf2:1`) (disarm, magical, reach 20 ft.), **Damage** 2d10+13 piercing"
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (agile, reach 15 ft., unarmed), **Damage** 2d8+13 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 30, attack +22<br>**4th** [[Vapor Form]]<br>**3rd** [[Levitate]] (At Will)<br>**2nd** [[Mist]] (At Will)"
abilities_bot:
  - name: "Crushing Cloud"
    desc: "`pf2:1` The cloud giant solidifies some clouds, including fog or mist, around a creature that's already in a cloud up to 120 feet away. The target takes 3d8 bludgeoning damage (DC 30 [[Fortitude]] save). If it fails its save, it treats clouds as difficult terrain for 1 round."
  - name: "Wind Strike"
    desc: "`pf2:2` The cloud giant Strikes a creature with their ranseur, surrounded in a roar of rushing air. On a hit, the target takes an additional 4d8 bludgeoning damage and is [[Deafened]] for 1 minute. Whether or not the Strike hits, each non-cloud giant within a @Template[emanation|distance:20], including the target of the Strike, is buffeted by roaring winds and must attempt a DC 30 [[Fortitude]] save saving throw. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes @Damage[2d8[sonic]|options:area-damage] damage. <br> - **Failure** The creature takes @Damage[4d8[sonic]|options:area-damage] damage and is deafened until the end of its next turn. <br> - **Critical Failure** As failure, but double damage and also knocked [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The graceful and regal cloud giants are fractious, with roughly half their clans believing they should rule over humanoids regardless of their size and the rest shying away from any contact with outsiders. Due to the physical and ideological distance between clans, most rely on giant eagle or roc messengers, to arrange marriages and exchange art without setting foot in each other's territory.

Cloud giants' skin color ranges from milky white to powdery blue. They make their homes anywhere veiled by the clouds, generally mountaintops or isolated valleys, but occasionally fog-shrouded swamps or misty rainforests. Legends persist of floating cities ruled by magically gifted cloud giant queens and kings. While most cloud giants plainly state that such claims are pure fantasy, others are mysteriously tight-lipped or evasive about the matter.

Giants are massive humanoid creatures who live in remote regions throughout the world. They vary widely but are united in their hunger, requiring sustenance of their own element along with the feasts one would expect from such a massive humanoid. Although a simple matter for some giants, more esoteric types find this need a harsh reality. While a massive fistful of ice or snow alongside their meal will satisfy a frost giant, shadow giants hunger for the coagulated shadows of the Netherworld.

```statblock
creature: "Cloud Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
