---
type: creature
group: ["Dero", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dero Magister"
level: "5"
rare_01: "Uncommon"
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
    desc: "+8; [[Darkvision]]"
languages: "Aklo, Sakvroth"
skills:
  - name: Skills
    desc: "Crafting +12, Medicine +10, Occultism +12, Stealth +11"
abilityMods: ["+1", "+4", "+2", "+3", "-1", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "22; **Fort** +10, **Ref** +13, **Will** +10"
health:
  - name: HP
    desc: "65; **Immunities** confused"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A dero magister takes 10 untyped damage for every hour they're exposed to sunlight."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +10 (`pf2:1`) (two hand d8), **Damage** 1d4+3 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 24, attack +16<br>**3rd** (3 slots) [[Blindness]], [[Levitate]], [[Vampiric Feast]]<br>**2nd** (4 slots) [[Laughing Fit]], [[Paranoia]], [[Stupefy]], [[Telekinetic Maneuver]]<br>**1st** (4 slots) [[Detect Magic]], [[Forbidding Ward]], [[Force Barrage]], [[Grim Tendrils]], [[Light]], [[Message]], [[Phantom Pain]], [[Soothe]], [[Void Warp]]"
  - name: "Occult Innate Spells"
    desc: "DC 24, attack +16<br>**4th** [[Nightmare]], [[Rewrite Memory]]<br>**2nd** [[Darkness]], [[Revealing Light]]<br>**1st** [[Daze]], [[Light]], [[Read Aura]]"
abilities_bot:
  - name: "Cytillesh Stare"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The magister focuses their gaze on a creature they can see within 30 feet. The target is [[Dazzled]] for 1 round and must succeed at a DC 24 [[Will]] save saving throw or be [[Confused]] for 1 round."
  - name: "Dero Medicine"
    desc: "`pf2:1` **Requirements** The dero is wearing a cytillesh toolkit and has a hand free <br>  <br> **Effect** The dero excises damaged flesh and crudely stitches wounds shut, healing themself or an ally in reach for @Damage[(2d8+10)[healing]]{2d8+10 Hit Points}. For 1 hour, the target has slashing weakness 2 and is immune to Dero Medicine. <br>  <br> > [!danger] Effect: Dero Medicine"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Dero magisters are leaders among dero society. They perform the bulk of the cruel operations and memory-altering procedures inflicted upon their victims.

Deros are short, wiry humanoids with milky white eyes, gray-blue skin, and wild shocks of off-white or gray hair. The descendants of a mysterious type of fey abandoned in the deepest, darkest caverns of Golarion, deros are the subject of fearful legends and folk tales to most of the world's surface races. They skulk beneath major metropolitan areas, performing cruel and twisted experiments on unwilling subjects.

Deros, particularly the leading magisters, are fixated with curing their allergy to sunlight. To understand how the surface dwellers can withstand the light of the sun, deros conduct late-night raids on surface cities, abducting victims and performing terrible experiments on them. Those who survive are often returned with much of their memory erased and their bodies bearing mysterious scars.

The largest dero settlements are built around esoteric machines of floating crystals. As these crystals grind against each other and hum with sickening blue energy, crystal flakes and powdery residue collect beneath the machinery. Dero magisters gather these products, creating tools and repurposing the crystals to power magical items.

```statblock
creature: "Dero Magister"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
