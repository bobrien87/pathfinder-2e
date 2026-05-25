---
type: creature
group: ["Dero", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dero Strangler"
level: "3"
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
    desc: "+6; [[Darkvision]]"
languages: "Aklo, Sakvroth"
skills:
  - name: Skills
    desc: "Athletics +11, Intimidation +7, Medicine +6, Stealth +10"
abilityMods: ["+4", "+3", "+3", "+0", "-1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +10, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "45; **Immunities** confused"
abilities_mid:
  - name: "Ill Glow"
    desc: "A non-dero living creature that starts its turn [[Grabbed]] or [[Restrained]] by the strangler is exposed to the sickly blue light from the strangler's cytillesh toolkit. It must succeed at a DC 19 [[Fortitude]] save or become [[Sickened]] 1. This has no effect if the strangler isn't wearing the toolkit."
  - name: "Vulnerable to Sunlight"
    desc: "A dero strangler takes 8 untyped damage for every hour they're exposed to sunlight."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spiked Chain +11 (`pf2:1`) (disarm, trip), **Damage** 1d8+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +10 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+2 piercing plus [[Lethargy Poison]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19, attack +11<br>**2nd** [[Darkness]], [[Revealing Light]]<br>**1st** [[Daze]], [[Light]], [[Read Aura]]"
abilities_bot:
  - name: "Dero Medicine"
    desc: "`pf2:1` **Requirements** The dero is wearing a cytillesh toolkit and has a hand free <br>  <br> **Effect** The dero excises damaged flesh and crudely stitches wounds shut, healing themself or an ally in reach for 2d8 Hit Points. For 1 hour, the target has slashing weakness 2 and is immune to Dero Medicine. <br>  <br> > [!danger] Effect: Dero Medicine"
  - name: "Strangle"
    desc: "`pf2:1` **Requirements** The dero must have two free hands or be wielding a spiked chain <br>  <br> **Effect** The dero attempts an Athletics check to [[Grapple]] with a +2 circumstance bonus. On a success, the target also takes @Damage[(1d6+6)[bludgeoning]] damage and can't speak (including to Cast a Spell) as long as they're [[Grabbed]] or [[Restrained]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Dero stranglers specialize in capturing living victims, and they are often called upon to aid in abductions.

Deros are short, wiry humanoids with milky white eyes, gray-blue skin, and wild shocks of off-white or gray hair. The descendants of a mysterious type of fey abandoned in the deepest, darkest caverns of Golarion, deros are the subject of fearful legends and folk tales to most of the world's surface races. They skulk beneath major metropolitan areas, performing cruel and twisted experiments on unwilling subjects.

Deros, particularly the leading magisters, are fixated with curing their allergy to sunlight. To understand how the surface dwellers can withstand the light of the sun, deros conduct late-night raids on surface cities, abducting victims and performing terrible experiments on them. Those who survive are often returned with much of their memory erased and their bodies bearing mysterious scars.

The largest dero settlements are built around esoteric machines of floating crystals. As these crystals grind against each other and hum with sickening blue energy, crystal flakes and powdery residue collect beneath the machinery. Dero magisters gather these products, creating tools and repurposing the crystals to power magical items.

```statblock
creature: "Dero Strangler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
