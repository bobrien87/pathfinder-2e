---
type: creature
group: ["Earth", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stygira"
level: "7"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Earth"
trait_02: "Fey"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17"
languages: "Aklo, Cyclops, Jotun, Petran"
skills:
  - name: Skills
    desc: "Athletics +15, Deception +15, Nature +17, Occultism +17, Gem Lore +17"
abilityMods: ["+4", "+4", "+5", "+4", "+6", "+2"]
abilities_top:
  - name: "Gemsight"
    desc: "As long as the stygira holds a gemstone, they can see through the gem with [[Darkvision]] and the effects of [[Truesight]]. A stygira is blind when they aren't holding a gem in a hand."
  - name: "Stone Curse"
    desc: "Wounds dealt by the stygira's claws leave the flesh bleached of color and turn the blood that runs from them dark gray. Each time a creature is damaged by the stygira's claw Strike, it must succeed at a DC 25 [[Fortitude]] save or become permanently [[Slowed]] 1 ([[Slowed]] 2 on a critical failure) as its flesh stiffens like stone. If a creature is reduced to 0 Hit Points from the stygira's claw Strike and fails the saving throw against stone curse, it's petrified. A creature that spends 8 hours in direct sunlight can attempt a new saving throw to remove the effects of stone curse, even if it has been petrified."
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +13, **Will** +19"
health:
  - name: HP
    desc: "80; **Immunities** paralyzed, petrified, visual; **Weaknesses** cold iron 5; **Resistances** physical 10 except adamantine"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Light Sickness"
    desc: "A stygira in an area of bright light is [[Sickened]] 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`) (agile), **Damage** 2d6+10 slashing plus [[Stone Curse]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Clairvoyance]], [[Read Omens]], [[Shape Stone]]<br>**3rd** [[Clairaudience]], [[Earthbind]]<br>**2nd** [[Augury]]<br>**1st** [[Know the Way]], [[Read Aura]]"
abilities_bot:
  - name: "Gem Gaze"
    desc: "`pf2:1` The stygira holds aloft a gem and gazes into the mind of a creature within 30 feet, infusing the creature's thoughts with visions of its own dead body slowly petrifying. The creature must succeed at a DC 25 [[Will]] save or become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These scarred, eyeless creatures appear as withered hermits wrapped in tattered rags. They can command strange secrets of the earth and interpret the fateful energies of the subterranean depths. In some regions, stygiras are worshipped as seers or even gods, although they lack the ability to grant spells to clerics and often aren't aware of their worshippers at all. In other areas, they have strange ties to the ancient empires of the cyclopes, frequently dwelling in the oversized ruins those creatures left behind long ago. To many stygiras, gemstones harvested from ancient cyclopean mosaics have even greater magical properties than other crystals.

Although technically blind, stygiras do have vestigial eyes hidden beneath the stony, scarred flesh of their faces. Capable of sensing bright lights even through their scars, stygiras are sickened and distracted by these flashing glimpses, so they keep to their caves during the day and only wander into the world above after nightfall. Far from benevolent, stygiras often waylay unwary travelers so they can reduce their victims down to the base chemicals and supernatural humors required to infuse their gemstones with the capacity to give them sight and magical power.

```statblock
creature: "Stygira"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
