---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ovinnik"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Intimidation +11, Stealth +13, Household Lore +12"
abilityMods: ["+0", "+5", "+0", "+2", "+5", "+3"]
abilities_top:
  - name: "Master of the Granary"
    desc: "A home with a friendly ovinnik is blessed, as the ovinnik preserves food from vermin and mold. <br>  <br> A home so blessed never suffers from random accidents such as fires, and any checks to [[Craft]], [[Earn Income]], [[Repair]], or [[Subsist]] in the home receive a +2 circumstance bonus. If the ovinnik is unfriendly, such checks take a -2 circumstance penalty instead, as the ovinnik causes devastating fires and infestations <br>  <br> An ovinnik must spend a week in a place before these benefits occur."
armorclass:
  - name: AC
    desc: "20; **Fort** +8, **Ref** +13, **Will** +11"
health:
  - name: HP
    desc: "60; **Weaknesses** cold iron 5; **Resistances** fire 5"
abilities_mid:
  - name: "Shy"
    desc: "An ovinnik is naturally [[Invisible]] while within sight of their bound home. The ovinnik can become visible, or even selectively visible-allowing some people to see them."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (agile, finesse, magical), **Damage** 2d6+3 slashing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21, attack +13<br>**4th** [[Read Omens]]<br>**2nd** [[Augury]], [[Floating Flame]]<br>**1st** [[Breathe Fire]], [[Cleanse Cuisine]] (At Will), [[Daze]], [[Ignition]]"
abilities_bot:
  - name: "Raise Grain Cloud"
    desc: "`pf2:2` While in their bound storeroom or granary, the ovinnik slams a paw against the ground, stirring up a cloud of grain dust in an @Template[emanation|distance:20]. <br>  <br> Within this cloud, they gain a +4 status bonus to any fire damage they deal. The ovinnik doubles their fire resistance against this increased damage. The grain cloud dissipates after the first such effect or after 1 minute if no such effects occur."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The ovinnik is the most ferocious of house spirits, and the only one that will kill if sufficiently angered. They live in granaries, storage rooms, and sheds where food—particularly grain—is kept. Ovinniks resemble bipedal cats but bark like a dog to scare away thieves, and they often demand gifts of milk, pancakes, and dead roosters.

House spirits are shy, often helpful, sometimes wrathful fey who dwell alongside peasants and farmers. They reside in the house, the yard, the granary, the bathhouse—wherever people build and live. Due to this proximity, house spirits often take on the mannerisms or appearance of nearby mortals. Their reclusive nature and tendency to go unseen earned them the moniker of "spirits," though in truth they're fully embodied fey.

House spirits take an almost parental interest in "their" mortals. Given proper respect, these fey work tirelessly for their charges—they chop wood, care for livestock, mend clothes, sweep the floor, and tend to the stove. If offended, though, the house spirit becomes a menace, frightening animals or children and ruining belongings.

```statblock
creature: "Ovinnik"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
