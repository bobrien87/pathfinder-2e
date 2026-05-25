---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Divine Warden of Pharasma"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15"
abilityMods: ["+5", "-2", "+4", "-5", "+0", "-5"]
abilities_top:
  - name: "Faithful Weapon"
    desc: "dagger, striking rune <br>  <br> A divine warden always wields its patron deity's favored weapon. If the weapon is a ranged weapon, the divine warden automatically generates new ammunition with each attack. For a divine warden of 4th level or higher, the deity's favored weapon gains the effects of a *[[Striking]]* rune while the divine warden wields it; at 12th level, these effects are of a *Greater Striking* rune, and at 19th level, they're instead of a *Major Striking* rune."
  - name: "Instrument of Faith"
    desc: "The divine warden is a beacon for its deity's faith. A cleric of the divine warden's patron deity can channel a [[Heal]] spell through a divine warden they can see within 60 feet. The cleric determines any targets or area for the spell as if they were standing in the divine warden's space."
armorclass:
  - name: AC
    desc: "24; **Fort** +17, **Ref** +11, **Will** +14"
health:
  - name: HP
    desc: "95"
abilities_mid:
  - name: "Divine Destruction"
    desc: "When the divine warden is reduced to 0 HP, it erupts with divine energy in a @Template[emanation|distance:30], dealing @Damage[7d6[spirit]|options:area-damage] damage per level. Each creature in the area must attempt a DC 21 [[Will]] save with the following outcomes. <br> - **Critical Success** The creature takes half damage. <br> - **Success** The creature takes full damage. <br> - **Failure** The creature takes full damage and becomes temporarily cursed by the patron deity. The creature becomes [[Enfeebled]] 1 and [[Stupefied 1]] for 1 day; this is a curse effect that uses the Will save DC as the counteract DC. <br> - **Critical Failure** As failure, except the creature becomes [[Enfeebled]] 2 and [[Stupefied 2]]."
  - name: "Faith Bound"
    desc: "A divine warden can't attack a creature that openly wears or displays the religious symbol of the divine warden's patron deity unless that creature uses a hostile action against the divine warden first. If the divine warden is intelligent, it can also attack a creature it believes isn't faithful to its deity or who wears the religious symbol as a ruse (typically after succeeding at a Perception check to [[Sense Motive]])."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +16 (`pf2:1`) (agile, magical, versatile s), **Damage** 2d4+7 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +13<br>**1st** [[Divine Lance]]"
  - name: "Divine Domain Spells"
    desc: "DC 21, attack +0<br>**1st** [[Death's Call]], [[Healer's Blessing]]"
abilities_bot:
  - name: "Mask of Fate"
    desc: "`pf2:2` The divine warden of Pharasma peers at a single creature within 60 feet through the eyes of its mask to alter its destiny. The target must attempt a DC 21 [[Will]] save. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target takes a –1 status penalty to the next saving throw it attempts within the next minute against a divine effect from a divine warden of Pharasma or worshipper of Pharasma. <br> - **Failure** For the next saving throw the target attempts within the next minute against a divine effect from a divine warden of Pharasma or worshipper of Pharasma, it rolls twice and takes the worse result. <br> - **Critical Failure** As failure, but the misfortune effect applies to all applicable saving throws."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This divine warden serves Pharasma, the goddess of birth, death, and fate. It protects a temple or shrine to the Lady of Graves.

```statblock
creature: "Divine Warden of Pharasma"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
