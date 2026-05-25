---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vloriak"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]]"
languages: "Chthonian, Common (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +13, Intimidation +12"
abilityMods: ["+4", "+2", "+4", "-1", "+4", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Rust"
    desc: "A vloriak's saliva causes metal to rust rapidly. If it succeeds at a tongue Strike or [[Disarm]] attempt, the vloriak deals 2d6 untyped damage (doubled on a critical hit) to a metal item the target is wearing or holding, ignoring its Hardness. If the vloriak hits an unattended metal item, the item takes this damage automatically. If a creature uses the Shield Block reaction with a metal shield against a tongue attack, the shield is automatically broken, but no other item is rusted on that attack."
  - name: "Tetanus"
    desc: "An infection introduced through open wounds, tetanus can produce stiffness, muscle spasms strong enough to break bones, and ultimately death. <br>  <br> **Saving Throw** DC 14 [[Fortitude]] save <br>  <br> **Onset** 10 days <br>  <br> **Stage 1** [[Clumsy]] 1 (1 week) <br>  <br> **Stage 2** [[Clumsy]] 2 and can't speak (1 day) <br>  <br> **Stage 3** [[Paralyzed]] with spasms (1 day) <br>  <br> **Stage 4** death"
armorclass:
  - name: AC
    desc: "21; **Fort** +15, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "90; **Weaknesses** cold iron 5, holy 5; **Resistances** acid 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Restoration Vulnerability"
    desc: "A vloriak feels agonizing pain when a creature or object recovers from a debilitating effect in their proximity. The first time in a round in which a creature that is within sight of the demon reduces the value of their clumsy, enfeebled, sickened, or stupefied condition, the demon takes 3d6 mental damage and cannot Lick Rust on their next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +15 (`pf2:1`) (unarmed, unholy), **Damage** 2d6+6 slashing plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Tongue +15 (`pf2:1`) (agile, reach 10 ft., unholy), **Damage** 1d6 spirit plus 2d6 acid plus [[Rust]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22, attack +14<br>**3rd** [[Paralyze]]<br>**2nd** [[Acid Grip]], [[Shatter]]<br>**1st** [[Caustic Blast]]"
abilities_bot:
  - name: "Lick Rust"
    desc: "`pf2:1` **Requirements** The vloriak rusted a metal item with its tongue this turn <br>  <br> **Effect** The vloriak attempts a tongue Strike on the same target it just attacked. If it hits, it deals no damage as it licks away the rust and heals 2d6 healing Hit Points (or 4d6 healing Hit Points if the Strike was a critical hit). It can't Lick Rust on its next turn."
  - name: "Spew Rusted Shards"
    desc: "`pf2:2` The vloriak spews a @Template[cone|distance:15] of acid and rusted metal. Creatures in the area take @Damage[3d6[acid],3d6[piercing]|options:area-damage]{3d6 acid and 3d6 piercing} damage (DC 22 [[Reflex]] save). A creature that takes any piercing damage is exposed to tetanus. The vloriak can't Spew Rusted Shards for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Vloriaks rise from the sinful souls of those whose acts of sabotage resulted in despair and terror, and they delight in the destruction of mortal artifice. They make use of their ability to rust metals to destroy structures, precious works of art, and tools used for creation. In combat, this ability allows them to destroy the armaments of their attacks. Vloriaks particularly enjoy destroying armors and shields, as these defensive items generally bear elegant designs and decorations that are more enjoyable to despoil than those of a weapon.

Often called despoiler demons, vloriaks were the followers of the long-dead demon lord Xar-Azmak. Their numbers have dwindled over the eons since the Lord of Rust's death; those that exist now are scattered throughout the Outer Rifts. Their chitinous bodies and faceted eyes give them an insectile appearance.

```statblock
creature: "Vloriak"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
