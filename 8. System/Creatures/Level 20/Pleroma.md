---
type: creature
group: ["Aeon", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pleroma"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+37; [[Darkvision]], [[Lifesense]] (imprecise) 120 feet, [[Truesight]] (precise) 60 feet"
languages: "Envisioning"
skills:
  - name: Skills
    desc: "Acrobatics +33, Arcana +38, Deception +34, Diplomacy +34, Occultism +38, Religion +39, Stealth +35"
abilityMods: ["+6", "+7", "+6", "+8", "+9", "+6"]
abilities_top:
  - name: "Envisioning"
    desc: "100 feet <br>  <br> A pleroma can communicate mentally with any creatures in the aura using wordless psychic projections. They don't need to share a language, though the aeon's meaning to non-aeons can be vague and is often mysterious. An aeon can use this ability to communicate flawlessly with any other aeon on the same plane as itself."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "45; **Fort** +32, **Ref** +31, **Will** +37"
health:
  - name: HP
    desc: "335; regeneration 20 (deactivated by spirit); **Immunities** vitality, void; **Weaknesses** spirit 20"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 20 (Deactivated by Spirit)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Reality Twist"
    desc: "`pf2:r` **Trigger** The pleroma critically fails a saving throw <br>  <br> **Effect** The critical failure becomes a normal failure."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Touch of Creation +36 (`pf2:1`) (agile, magical, vitality), **Damage** 5d8+16 vitality"
  - name: "Melee strike"
    desc: "Touch of Destruction +36 (`pf2:1`) (agile, magical, void), **Damage** 5d8+16 void"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 47, attack +39<br>**10th** [[Manifestation]]<br>**9th** [[Detonate Magic]], [[Overwhelming Presence]]<br>**8th** [[Unrelenting Observation]]<br>**7th** [[Interplanar Teleport]], [[Retrocognition]]<br>**6th** [[Blessed Boundary]], [[Disintegrate]], [[Truesight]] (Constant)<br>**5th** [[Banishment]]<br>**4th** [[Creation]] (At Will), [[Shape Stone]] (At Will), [[Unfettered Movement]] (Constant)<br>**3rd** [[Hypercognition]] (At Will)<br>**2nd** [[Create Food]] (At Will), [[Shape Wood]] (At Will)<br>**1st** [[Create Water]] (At Will), [[Vitality Lash]], [[Void Warp]]"
abilities_bot:
  - name: "Generate Sphere"
    desc: "`pf2:2` The pleroma manifests a 2-foot-diameter sphere of energy—either a white sphere of creation that hovers above their left hand or a black sphere of oblivion above their right. This action has the vitality trait for a sphere of creation or the void trait for a sphere of oblivion. A sphere vanishes after 1 minute, when it is more than 300 feet from the pleroma, or when the pleroma Generates a Sphere of that type again. A sphere of oblivion winks out of existence when it vanishes, but a sphere of creation explodes in blinding light—each creature in a @Template[emanation|distance:30] must succeed at a DC 43 [[Fortitude]] save or be permanently [[Blinded]]. This is a light effect."
  - name: "Propel Sphere"
    desc: "`pf2:1` **Requirements** The pleroma has a sphere of creation or sphere of oblivion active <br>  <br> **Effect** The pleroma makes one of its spheres fly 10 feet in any direction, ignoring difficult terrain and greater difficult terrain. A sphere of creation creates new matter in its path, which the pleroma can have manifest as normal terrain, difficult terrain, greater difficult terrain, or a cube of solid mater (such as clay, wood, or stone). A sphere of oblivion destroys unattended objects it touches, though larger objects are destroyed at a rate of one 10-foot cube per round of contact. The sphere can enter the space of a creature; when it does, the creature takes 20d6 damage with a DC 43 [[Fortitude]] save. <br>  <br> This is an incapacitation effect. <br> - **Success** The creature takes no damage and is pushed out of the sphere to the nearest open space of the GM's choice. <br> - **Failure** The creature takes full damage; this is vitality damage for a sphere of creation or void damage for a sphere of oblivion, but it can damage any type of creature regardless of its normal immunities. The creature is then pushed out of the sphere as on a success. A creature reduced to 0 HP is slain instead of being pushed out, either merged with new matter for a sphere of creation or completely destroyed for a void of oblivion; the creature can be restored only via a [[Wish]] ritual or similarly powerful effect. This is a death effect. <br> - **Critical Failure** As failure, but the creature takes double damage."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Among the most powerful of all the true aeons, pleromas are the ultimate manifestation of the duality of creation and destruction. Their physical manifestation is a constant state of flux between these two extremes; their forms are draped in a hooded, shifting cloak of night black where galaxies and other celestial objects flit in and out of existence at every moment, as if depicting the constant life, death, and rebirth of a miniature, self-contained universe.

Pleromas see the multiverse as both eternal and cyclical, doomed and malleable, ending only if these cycles ever become unbalanced. They believe the current Convergence is necessary to obtain this essential balance, and act to ensure that the grand design of the Monad is carried out to the smallest detail.

Aeons have always been the caretakers of reality and defenders of the natural order of balance. Each type of aeon takes on some form of duality in its manifestation and works either to shape the multiverse within the aspects of this duality in some way, or to correct imbalances to the perfect order of existence. Aeons' machinations can raise a nation, raze it, or restore it from ruin. Their reasons are their own, and they rarely share their motivations with others—through their strange envisioning mode of communication, they simply create the results they insist are necessary to maintain the balance of the multiverse.

As a result of recent shifts in reality, aeons have begun to reassert a presence in the perfect planar city of Axis. To aeons, this is merely the latest in a recurring cycle, albeit one that mortals have not yet borne witness to. Aeons have a name for this cyclic return, in which they welcome their industrious axiomite brethren back to their fold: the Convergence. At the onset of the Convergence, a council of pleroma aeons appeared in the Eternal City of Axis, where they revealed that axiomites were wayward aeons, split off long ago to pursue the act of creation. With the latest cycle of change, it was time for axiomites—and their mortal creations and kin—to rejoin the aeon cause. While most axiomites fell in line, realizing perhaps on a fundamental level of reality that what the aeons said was the truth, some refused to heed the call and waited for the wrath of the aeons. That wrath has yet to come. The dual-natured aeons have responded to those who have declined in confusing ways. With some they treat and even bargain, while a handful of others they have destroyed, and a few have been exterminated by the axiomites. But most of these quiet insurgents they leave alone, allowing these axiomites to continue to create in peace. How—or if—this Convergence will end is as little understood as aeons themselves.

```statblock
creature: "Pleroma"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
