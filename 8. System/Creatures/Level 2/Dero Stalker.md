---
type: creature
group: ["Dero", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dero Stalker"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Dero"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: "Aklo, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +8, Medicine +5, Stealth +8, Thievery +8"
abilityMods: ["+2", "+4", "+3", "+0", "-1", "+1"]
abilities_top:
  - name: "Exploit Lethargy"
    desc: "A creature afflicted with [[Lethargy Poison]] is [[Off Guard]] to the dero stalker, and the stalker can choose to add the nonlethal trait to their attacks against the creature without taking the normal penalty."
  - name: "Sneak Attack"
    desc: "A dero stalker deals 1d6 extra precision damage to creatures who are [[Off Guard]]."
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +10, **Will** +3"
health:
  - name: HP
    desc: "30; **Immunities** confused"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A dero stalker takes 4 untyped damage for every hour they're exposed to sunlight."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +8 (`pf2:1`), **Damage** 1d6+2 bludgeoning"
  - name: "Melee strike"
    desc: "Club +10 (`pf2:1`) (thrown 10), **Damage** 1d6+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +10 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6 piercing plus [[Lethargy Poison]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 17, attack +9<br>**1st** [[Daze]], [[Light]], [[Read Aura]]"
abilities_bot:
  - name: "Dero Medicine"
    desc: "`pf2:1` **Requirements** The dero is wearing a cytillesh toolkit and has a hand free <br>  <br> **Effect** The dero excises damaged flesh and crudely stitches wounds shut, healing themself or an ally in reach for 2d8 Hit Points. For 1 hour, the target has slashing weakness 2 and is immune to Dero Medicine. <br>  <br> > [!danger] Effect: Dero Medicine"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Dero stalkers explore the surface world by night, seeking out victims to abduct. While hiding from the burning light of day, stalkers often assist with magisters' experiments.

Deros are short, wiry humanoids with milky white eyes, gray-blue skin, and wild shocks of off-white or gray hair. The descendants of a mysterious type of fey abandoned in the deepest, darkest caverns of Golarion, deros are the subject of fearful legends and folk tales to most of the world's surface races. They skulk beneath major metropolitan areas, performing cruel and twisted experiments on unwilling subjects.

Deros, particularly the leading magisters, are fixated with curing their allergy to sunlight. To understand how the surface dwellers can withstand the light of the sun, deros conduct late-night raids on surface cities, abducting victims and performing terrible experiments on them. Those who survive are often returned with much of their memory erased and their bodies bearing mysterious scars.

The largest dero settlements are built around esoteric machines of floating crystals. As these crystals grind against each other and hum with sickening blue energy, crystal flakes and powdery residue collect beneath the machinery. Dero magisters gather these products, creating tools and repurposing the crystals to power magical items.

```statblock
creature: "Dero Stalker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
