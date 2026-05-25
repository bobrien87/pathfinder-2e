---
type: creature
group: ["Divine", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deific Vessel of Urgathoa"
level: "15"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Divine"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Lifesense]] (precise) 60 feet"
languages: "Common, Necril (truespeech)"
skills:
  - name: Skills
    desc: "Athletics +26, Deception +27, Intimidation +29, Religion +31, Undead Lore +33"
abilityMods: ["+5", "+4", "+6", "+2", "+4", "+6"]
abilities_top:
  - name: "Mark of Fate"
    desc: "A creature that slays the deific vessel must succeed at a DC 35 [[Will]] save or be visibly marked as anathema to [[Urgathoa]]. It gains weakness 10 to unholy and takes a –2 circumstance penalty to Charisma-based skill checks against followers of Urgathoa. Creatures attempting to [[Gather Information]] about or [[Track]] the marked creature gain a +2 circumstance bonus to their checks. <br>  <br> The mark can't be hidden and can be removed only by participating in an atone ritual led by a worshipper of Urgathoa who is 12th level or higher. <br>  <br> > [!danger] Effect: Mark of Fate"
  - name: "Grave Chill"
    desc: "The vessel's unarmed attacks and scythe gain the *+2 [[Decaying]] [[Frost]] greater striking* runes when used by the vessel, and their Strikes gain the death trait."
armorclass:
  - name: AC
    desc: "35; **Fort** +28, **Ref** +24, **Will** +26"
health:
  - name: HP
    desc: "300; **Immunities** death effects, disease, paralyzed, unconscious; **Weaknesses** holy 15; **Resistances** void 15"
abilities_mid:
  - name: "Limited Lifespan"
    desc: "The deific vessel takes 25 untyped damage at the end of its turn if it Cast a Spell, used Borrow Time, or made a Strike that turn. This damage ignores resistance."
  - name: "Shattered Vessel"
    desc: "When the deific vessel dies, the divine power barely contained within their form explodes outward, dealing @Damage[6d8[spirit]|options:area-damage] damage to each creature in a @Template[type:emanation|distance:30] with a DC 33 [[Reflex]] save."
  - name: "Void Tendrils"
    desc: "30 feet. <br>  <br> When a creature in the aura would be healed by a vitality effect, the healing is reduced by 15 and the deific vessel regains 15 healing Hit Points."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Decaying Frost Scythe +28 (`pf2:1`) (deadly d10, magical, trip, unholy), **Damage** 3d10+11 slashing"
  - name: "Melee strike"
    desc: "Decaying Frost Fist +28 (`pf2:1`) (agile, magical, unarmed, unholy), **Damage** 3d4+11 bludgeoning"
  - name: "Ranged strike"
    desc: "Grave Pulse +27 (`pf2:1`) (cold, unholy, void), **Damage** 3d6 cold plus 2d8 void"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 39, attack +31<br>**7th** [[Divine Decree]], [[Eclipse Burst]], [[Execute]], [[Mask of Terror]]<br>**6th** [[Dominate]], [[Truesight]], [[Vampiric Exsanguination]], [[Zealous Conviction]]<br>**5th** [[Truespeech]] (Constant)<br>**1st** [[Detect Magic]], [[Divine Lance]], [[Harm]], [[Harm]] (At Will), [[Message]]"
abilities_bot:
  - name: "Borrow Time"
    desc: "`pf2:1` The vessel chooses two different creatures in their void tendrils aura. Each one must be either undead or the vessel themself. One target loses 25 untyped HP and the other regains that many HP. If a target is unwilling, it can negate the transfer with a successful DC 39 [[Fortitude]] save."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Through direct intervention in the mortal world, a deity creates a deific vessel to do their will, whether from a willing servant or through possession, a contract, or a curse. A candle to the flame of their progenitor, a divine vessel burns fast and quickly extinguishes.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Deific Vessel of Urgathoa"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
