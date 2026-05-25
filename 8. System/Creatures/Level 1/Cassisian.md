---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cassisian"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +6, Diplomacy +6, Religion +6, Stealth +6"
abilityMods: ["-1", "+1", "+2", "-1", "+1", "+1"]
abilities_top:
  - name: "Repository of Lore"
    desc: "While the cassisian isn't particularly intelligent, they have perfect memory and can remember everything they see or hear. This allows them to attempt Lore checks on any topic, provided (at the GM's discretion) they've encountered the topic in question before. The cassisian's limited intellect often prevents them from acting upon their knowledge, making them a better resource than agent in using information."
armorclass:
  - name: AC
    desc: "16 +1 status vs. unholy creatures; **Fort** +7, **Ref** +6, **Will** +4"
health:
  - name: HP
    desc: "20; **Weaknesses** unholy 3; **Resistances** cold 3, fire 3"
abilities_mid:
  - name: "+1 Status to All Saves vs. Unholy Creatures"
    desc: ""
  - name: "+1 Status to AC vs. Unholy Creatures"
    desc: ""
  - name: "Transfer Protection"
    desc: "A creature can wear a willing cassisian as a helmet. While it does, the cassisian can't act, but the cassisian extends their +1 status bonus to AC and saves against unholy creatures to their wearer. At any time, the cassisian can detach themself from their wearer as a single action. <br>  <br> > [!danger] Effect: Transfer Protection"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Headbutt +6 (`pf2:1`) (agile, finesse, holy, magical, reach 0 ft.), **Damage** 1d6-1 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16, attack +8<br>**4th** [[Read Omens]]<br>**1st** [[Heal]], [[Know the Way]], [[Light]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` A cassisian can take the appearance of a dove, a winged humanoid, a dog, or a fish. Normally, this doesn't change their Speed or the attack and damage bonuses for their Strikes, but it might change the damage type Strikes deal (typically to bludgeoning). Any further changes for specific forms are noted below. <br>  <br> - **Dog** <br>  <br> - **Size** Small; <br> - [[Scent (Imprecise) 30 feet]], <br> - **Speed** 40 feet; <br> - **Skills** Athletics +6; <br> - **Melee** `pf2:1` jaws +7, **Damage** 1d6+2 piercing plus [[Knockdown]] <br>  <br> - **Fish** <br>  <br> - **Speed** Swim 30 feet <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Eye Beams"
    desc: "`pf2:2` The cassisian releases beams of heat or cold from their eyes, dealing 2d6 @Damage[2d6[cold]|options:area-damage]{cold} or @Damage[2d6[fire]|options:area-damage]{fire} damage (DC 17 [[Reflex]] save) to all creatures in a @Template[line|distance:15]. They can't use Eye Beams again for 1d4 rounds."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The weakest of angels, cassisians usually serve as lackey messengers for more powerful angels or as spiritual guides for mortals. Despite their limited intellect, cassisians have a knack for precise recollection, particularly with scripture. Most cassisians are formed from the souls of trustworthy mortals, but some arise from fragments of greater angels destroyed in service to the celestial realms.

The celestial hosts of angels are messengers and warriors, divided into choirs based on their abilities and purviews. Angels were one of the first creations of the gods, and many still assist their righteous creators throughout the cosmos. Most angels in modern times are not direct creations of the divine, however, instead consisting of ascended mortal souls drawn from the celestial planes.

The majority of unaffiliated angels live in Nirvana, the plane of virtue and enlightenment. Angels who are affiliated with deities dwell in those deities' domains or other areas where that god holds influence. Regardless of residence or service, angels remain benevolent messengers possessed with magical auras to aid their allies.

```statblock
creature: "Cassisian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
