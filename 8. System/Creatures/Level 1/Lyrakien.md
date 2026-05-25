---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lyrakien"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +9, Diplomacy +6, Performance +8, Religion +6, Stealth +7"
abilityMods: ["-2", "+4", "+1", "+1", "+3", "+3"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "17; **Fort** +4, **Ref** +7, **Will** +6"
health:
  - name: HP
    desc: "25; **Weaknesses** cold iron 3, unholy 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, finesse, holy, magical, reach 0 ft., unarmed), **Damage** 1d4-2 bludgeoning"
  - name: "Ranged strike"
    desc: "Starlight Ray +7 (`pf2:1`) (holy, light), **Damage** 2d4 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens]], [[Unfettered Movement]] (Constant)<br>**1st** [[Daze]], [[Detect Magic]], [[Heal]], [[Illusory Object]], [[Light]]"
abilities_bot:
  - name: "Starlight Blast"
    desc: "`pf2:2` The lyrakien unleashes a blast of holy starlight in a @Template[emanation|distance:5]. Enemies in the area take @Damage[2d6[spirit]|options:area-damage] damage with a DC 17 [[Reflex]] save. The lyrakien can't use Starlight Blast or their starlight ray ranged attack for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Lyrakiens are musical messengers and embodiments of free travel. They serve Desna and other deities and empyreal lords of Elysium but are quite fond of free time as a fundamental concept and are always on the hunt for opportunities to pause in their duties to enjoy music or appreciate a moment of beauty. They love contests, stories, and songs, and they often challenge mortals to musical contests or pester them to share grand tales of their exploits. Lyrakiens rely on their agility to avoid conflicts, but they do their best to defend places of great natural beauty, especially against foes they can damage with their starlight. Lyrakiens have an innate wanderlust and rarely stay in the same place for very long. Some travel alongside adventurers, often writing songs about their quests and feats of derring-do.

Though light-hearted creatures, lyrakiens don't let their whimsical personalities get in the way of protecting breathtaking natural locations. Sometimes called "glistenwings" by gnomes and halflings, they are frequently mistaken for sprites or similar fey, a bit of confusion that many lyrakiens find amusing and fertile ground for shenanigans involving those they deem deserving of a bit of unexpected fun and discord in their lives.

Azatas are manifestations of freedom and unestrained joy—kindly celestials with a penchant for curious exploration, spontaneous revelry, and whimsical quests. Born of good dreams and heartfelt wishes for a better world, they reside in the untamable wilds of Elysium. Azatas are passionate and mercurial, as beautiful and bright as a child's fantasy, but also fiercely loyal to those they hold dear. They act quickly and directly against fiendish and foul influences, but they tend to avoid guiding mortal affairs otherwise, allowing people to choose their own destiny without the meddling of otherworldly forces.

Azatas reject the dual chains of both duty and tyranny, but also the heavy chains of despair that reality so often inflicts upon those who live in it. This can give them a dubious reputation with other celestials, who consider azatas to be flighty and unreliable, but azatas know that unrelenting self-sacrifice can be just as destructive to the soul as evil. Azatas refuse to compromise the beauty of the world with such banality, instead living without regret and savoring every triumph and agony they encounter upon the way.

```statblock
creature: "Lyrakien"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
