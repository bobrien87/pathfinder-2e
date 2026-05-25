---
type: creature
group: ["Humanoid", "Tengu"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tengu Sneak"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: "Common, Tengu (plus two others)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +6, Deception +7, Diplomacy +5, Society +5, Stealth +8, Thievery +8"
abilityMods: ["+2", "+4", "+1", "+1", "+0", "+1"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The tengu deals an additional 1d6 precision damage to [[Off Guard]] creatures."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted yet are [[Off Guard]] to the tengu."
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +10, **Will** +4"
health:
  - name: HP
    desc: "27"
abilities_mid:
  - name: "Eat Fortune"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** A creature within 60 feet uses a fortune or misfortune effect <br>  <br> **Effect** The tengu negates the attempt to manipulate fate and fortune. Eat Fortune gains the opposing trait, and the triggering effect is disrupted."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +10 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+2 piercing"
  - name: "Melee strike"
    desc: "Wakizashi +10 (`pf2:1`) (agile, deadly d8, finesse, versatile p), **Damage** 1d4+2 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +10 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot:
  - name: "Feather Fan Dustup"
    desc: "`pf2:1` **Frequency** once per 10 minutes; <br>  <br> **Effect** The tengu waves their feather fan, summoning a small magical breeze that kicks up dust in a @Template[burst|distance:5] centered on a corner of their space, which lasts for 1d4 rounds. All creatures within that area are [[Concealed]], and all other creatures are concealed to them."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Tengu are an adaptable people originally from the continent of Tian Xia, but whose travels have taken them across all of Golarion. As a people in diaspora, tengu are almost always found within larger kingdoms and communities of other peoples, with the exception of their home nation of Kwanlai. As a result, tengu tend to gather in close-knit social groups both with other tengu as well as with other peoples of non-majority ancestries, collecting words and customs from other cultures the way a bird collects trinkets for its nest.

Although humanoid, tengu have very distinct, birdlike features, and many would say that they resemble crows more than they do humans. They have strong, thick beaks, as well as sharp talons at the ends of their arms and legs. Most of a tengu's body is covered in small feathers that range in color from dark brown and midnight blue to glossy black, with lighter colors being rare but not unheard of. Like many avian creatures, tengu have hollow bones, making them much lighter than other humanoids of their size, and some tengu even possess wings that allow them to fly.

Tengu have a strong cultural focus on the sky, considering tall mountaintops sacred places and worshipping gods associated with nature and storms, like Gozreh or Hei Feng. They have a long and proud tradition of both martial arts and smithing, and many aspiring Tian heroes have sought out a tengu mentor or swordsmith. Tengu magic revolves around using tengu feathers, bound into a fan, as a medium to command wind and lightning, and some tengu even have the power to "eat" misfortune—skills that only help tengu as they continue expanding across Golarion to new lands.

```statblock
creature: "Tengu Sneak"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
