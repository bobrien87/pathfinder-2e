---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aeolaeka"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Earth"
trait_04: "Holy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Darkvision]], [[Tremorsense]] (precise) 60 feet"
languages: "Draconic, Empyrean, Petran (Speak with Stones, Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +25, Diplomacy +22, Intimidation +22, Nature +23"
abilityMods: ["+6", "+4", "+7", "+2", "+5", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Earth Glide"
    desc: "An aeolaeka can Burrow through any earthen matter, including rock. When they do so, the aeolaeka moves at their full burrow Speed, leaving no tunnels or signs of their passing."
armorclass:
  - name: AC
    desc: "33; **Fort** +25, **Ref** +20, **Will** +23"
health:
  - name: HP
    desc: "250; **Weaknesses** cold iron 15, unholy 15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Warhammer +25 (`pf2:1`) (holy, magical, shove), **Damage** 2d8+12 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24<br>**6th** [[Petrify]]<br>**5th** [[Speak with Stones]] (Constant), [[Truespeech]] (Constant), [[Wall of Stone]]<br>**4th** [[Weapon Storm]]<br>**3rd** [[Earthbind]] (At Will), [[Locate]]<br>**2nd** [[Sure Footing]]<br>**1st** [[Heal]]"
abilities_bot:
  - name: "Liberate the Earth"
    desc: "`pf2:2` The aeolaeka conjures churning stones, creating a @Template[line|distance:60] of rolling boulders. Creatures in the line take @Damage[10d6[bludgeoning]|options:area-damage] damage with a DC 35 [[Reflex]] save. The area is difficult terrain for 24 hours before the leftover stone crumbles to dust. The aeolaeka can't Liberate the Earth for 1d4 rounds. <br> - **Critical Success** The creature takes no damage. <br> - **Success** The creature takes half damage. <br> - **Failure** The creature takes full damage and is knocked [[Prone]]. <br> - **Critical Failure** The creature takes double damage, is knocked prone, and is [[Immobilized]] by the rubble (`act escape dc=32`)."
  - name: "Statue"
    desc: "`pf2:1` Until the next time they act, the aeolaeka appears to be a statue. They have an automatic result of 45 on Deception checks and DCs to pass as a statue."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Aeolaekas, also known as stone azatas, embody the joy of stone carved by artists' hands or natural forces. Stone is often thought to be steadfast and unchanging, but, when viewed on a grander scale over vast periods of time, it can transform into things as diverse as intricate crystals and fine powder. Aeolaekas are fascinated by the gradual changes found within stone, from sand to diamonds to fossils to towering mountains.

As a result of their stone affinity, aeolaekas appear less capricious than other azatas—though this is mainly due to them acting on a different geological scale—and some have willingly forged lasting accords or agreements with mortals. Aeolaekas often visit the Plane of Earth, fighting against evil earth elementals, joining jabali festivals, or simply wandering the veins and tunnels of that realm as they bask in its stony wonders. Their stone skin means aeolaekas are sometimes mistaken for statues; they use this fact to hide in plain sight when they don't want their presence known.

Azatas are manifestations of freedom and unestrained joy—kindly celestials with a penchant for curious exploration, spontaneous revelry, and whimsical quests. Born of good dreams and heartfelt wishes for a better world, they reside in the untamable wilds of Elysium. Azatas are passionate and mercurial, as beautiful and bright as a child's fantasy, but also fiercely loyal to those they hold dear. They act quickly and directly against fiendish and foul influences, but they tend to avoid guiding mortal affairs otherwise, allowing people to choose their own destiny without the meddling of otherworldly forces.

Azatas reject the dual chains of both duty and tyranny, but also the heavy chains of despair that reality so often inflicts upon those who live in it. This can give them a dubious reputation with other celestials, who consider azatas to be flighty and unreliable, but azatas know that unrelenting self-sacrifice can be just as destructive to the soul as evil. Azatas refuse to compromise the beauty of the world with such banality, instead living without regret and savoring every triumph and agony they encounter upon the way.

```statblock
creature: "Aeolaeka"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
