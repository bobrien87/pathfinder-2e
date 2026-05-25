---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shemhazian"
level: "16"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]], [[Scent]] (imprecise) 60 feet, [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Draconic, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +31, Deception +25, Intimidation +27, Medicine +28, Religion +30"
abilityMods: ["+9", "+5", "+7", "+0", "+6", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Enfeebling Bite"
    desc: "If the shemhazian's jaws Strike damages a creature, the target is [[Enfeebled]] 3 for 24 hours. The target can attempt a DC 37 [[Fortitude]] save to reduce this to [[Enfeebled]] 1 (or be unaffected on a critical success)."
armorclass:
  - name: AC
    desc: "39; **Fort** +32, **Ref** +26, **Will** +27"
health:
  - name: HP
    desc: "350; **Weaknesses** cold iron 15, holy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Paralyzing Gaze"
    desc: "30 feet. <br>  <br> A non-demon creature that ends its turn in the aura must attempt a DC 35 [[Fortitude]] save. If it fails, it's [[Slowed]] 1 for 1 round, and if it critically fails, it is [[Paralyzed]] for 1 round."
  - name: "Succor Vulnerability"
    desc: "A shemhazian's mutilation is a part of them, and they can't bear to see it reversed. The first time each round that a creature heals from damage the shemhazian dealt on their last turn, the demon takes 3d6 mental damage."
  - name: "Tail Whip"
    desc: "`pf2:r` **Trigger** A creature within reach of the shemhazian's tail leaves a square during a move action it's using <br>  <br> **Effect** The shemhazian attempts to `act trip` the triggering creature. On a success, the creature also takes damage as if the shemhazian had hit with a tail Strike, and if the creature was flying, it falls 30 feet."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +33 (`pf2:1`) (magical, reach 20 ft., unarmed, unholy), **Damage** 3d12+17 piercing plus [[Enfeebling Bite]]"
  - name: "Melee strike"
    desc: "Claw +33 (`pf2:1`) (agile, magical, reach 20 ft., unarmed, unholy), **Damage** 3d8+17 slashing"
  - name: "Melee strike"
    desc: "Pincer +33 (`pf2:1`) (magical, reach 20 ft., unholy), **Damage** 3d8+17 bludgeoning plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Tail +33 (`pf2:1`) (magical, reach 30 ft., unholy), **Damage** 3d6+17 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29<br>**7th** [[Divine Decree]]<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Scouting Eye]]<br>**4th** [[Clairvoyance]], [[Translocate]], [[Translocate]] (At Will)<br>**2nd** [[Invisibility]] (At Will)"
abilities_bot:
  - name: "Focused Gaze"
    desc: "`pf2:1` The shemhazian focuses their gaze on a non-demon creature they can see within 30 feet. If that creature isn't already [[Slowed]] by the shemhazian's paralyzing gaze, it must attempt a save against the shemhazian's paralyzing gaze. If that creature is slowed, it must succeed at a DC 35 [[Fortitude]] save or be [[Paralyzed]] for 1 round. <br>  <br> A shemhazian can't use this ability against the same creature more than once per round."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Shemhazians rise from the souls of torturers and those who reveled in mutilating the physical bodies of their victims. Standing 35 feet tall, a shemhazian is well equipped with a wide range of claws, pincers, and fangs to continue inflicting such torments on those they encounter.

Shemhazians delight in tormenting mortals, of course, but more than most demons, they revel in sharing the pain with their own kind. Other demons fear and hate shemhazians for this reason, with only the most powerful willing to work with a shemhazian to achieve a shared goal. Even then, the shemhazian is always on the watch for an opportunity to bring pain and suffering to their allies along with any foe.

When a sinful mortal soul is judged and sent on to the Outer Rifts, it can become a deadly fiend—a demon. Demons are living incarnations of sin—be they classic sins like wrath or gluttony, or more "specialized" depravities like an obsession with torture or the act of treason or treachery. Once formed, a demon's driving goals are twofold—the amassing of personal power, and the corruption of mortal souls to cause them to become tainted by sin. In this way demons ensure a never-ending supply of new demons to bolster their ever-growing ranks in the Outer Rifts.

Demons are selfish and self-absorbed creatures, and most firmly believe that mortals only play at being more virtuous than fiends. They enjoy tempting mortals into damnation to both indulge their egos and swell their armies. Like many other fiends, one of the great rewards of this manipulation is fulfilling their hunger for souls. In their eyes, the primary use for these souls is to spawn new demons, who can serve as soldiers, slaves, pawns, or even currency for their more powerful masters.

```statblock
creature: "Shemhazian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
