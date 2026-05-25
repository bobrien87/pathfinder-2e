---
type: creature
group: ["Humanoid", "Vanara"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vanara Disciple"
level: "1"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Vanara"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: "Common, Fey, Vanara"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +4, Religion +4, Stealth +7"
abilityMods: ["+1", "+4", "+0", "+1", "+3", "+0"]
abilities_top:
  - name: "Prehensile Tail"
    desc: "The vanara can use their long, flexible tail to perform Interact actions requiring a free hand, even if both hands are otherwise occupied. Their tail can't perform actions that require fingers or significant manual dexterity, including any action that would require a check to accomplish, and they can't use it to hold items."
armorclass:
  - name: AC
    desc: "19; **Fort** +5, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "16"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, finesse, nonlethal), **Damage** 1d6+1 bludgeoning"
  - name: "Melee strike"
    desc: "Bo Staff +4 (`pf2:1`) (parry, reach 10 ft., trip), **Damage** 1d8+1 bludgeoning"
  - name: "Melee strike"
    desc: "Javelin +7 (`pf2:1`) (thrown 30), **Damage** 1d6+1 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 13, attack +5<br>**1st** [[Pest Form (Monkey Only)]]"
abilities_bot:
  - name: "Flurry of Blows"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The vanara disciple makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses."
  - name: "Spring Up"
    desc: "`pf2:2` **Requirements** The vanara disciple is [[Prone]] <br>  <br> **Effect** The vanara Stands, then can immediately Step twice. The Stand action doesn't trigger reactions."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Many young vanaras travel, both to see the world and to search for a path that might lead to enlightenment.

Vanaras are monkey-like humanoids who dwell in treetop villages high in the canopies of lush jungles and verdant forests. Like the monkeys they resemble, vanaras manifest a wide variety of different fur colors, body types, and facial features, but they all have in common long, dexterous fingers and toes as well as nimble and curious minds. Many of them learn to use their tails to capably manipulate objects.

Vanaras have a friendly culture, with most individuals seeking balance or enlightenment in their lives. Their propensity for mischief and history of fighting evil has earned them many ancestral enemies, and thus they usually make their homes far from urban areas. The majority of vanara settlements are found in southeastern Casmaron, among the lush jungles where they first originated. Devotion to monastic training and religious study has led to secondary populations forming in the Impossible Kingdom of Jalmeray, eastern Katapesh, Tian Xia, and northeastern Nex. Nonetheless, young vanaras seized by wanderlust might roam far across the world, and travelers from many distant lands might in turn visit vanara communities in search of the wisdom of their elders and sages.

Vanara culture often pits their inborn desire for trickery with a desire to transcend such origins, leading to many vanaras studying monastic practices. They also value tales of heroic vanaras from the past, looking to such icons for inspiration in their own lives. Most vanaras are quick to offer aid to those in distress and rarely hesitate in the face of evil, no matter the danger it presents. The leaders of vanara villages tend to be religious figures, or occasionally others possessing similar values and experience. Vanaras venerate Ragdya, the Sage of the Mountain, who encourages seeking enlightenment through worldly action and sees the virtues of pranks and humor.

```statblock
creature: "Vanara Disciple"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
