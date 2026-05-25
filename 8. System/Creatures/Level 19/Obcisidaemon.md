---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Obcisidaemon"
level: "19"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+35; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +33, Athletics +39, Deception +34, Intimidation +36, Religion +32, Warfare Lore +36"
abilityMods: ["+10", "+4", "+8", "+4", "+5", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Cloak of Souls"
    desc: "An obcisidaemon is shrouded at all times in a cloak of captured souls. It can hold a number of souls equal to the daemon's Charisma modifier. Destroying the daemon frees the souls, though this doesn't return the deceased creatures to life. A creature whose soul is trapped within this cloak can't be resurrected except by a 9th-rank [[Resurrect]] ritual or similarly powerful magic."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "43; **Fort** +35, **Ref** +29, **Will** +32"
health:
  - name: HP
    desc: "425; **Immunities** death effects; **Weaknesses** holy 20"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Scorched Earth"
    desc: "60 feet. Any creature who dies within the aura and isn't drawn into the obcisidaemon's Cloak of Souls via Inherit Soul must attempt a DC 38 [[Fortitude]] save. On a failure, the creature's body (but not its gear) is immediately reduced to a fine smear of ashes."
  - name: "Inherit Soul"
    desc: "`pf2:r` **Trigger** The obcisidaemon slays a creature <br>  <br> **Effect** The obcisidaemon attempts to draw the creature's soul into its cloak of souls. The triggering creature must attempt a DC 38 [[Fortitude]] save. On a failure, its soul is consumed and added to the cloak of souls. If the obcisidaemon's cloak can't hold any more souls, the daemon can release one of the souls as a free action; otherwise, the soul isn't absorbed."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Halberd +36 (`pf2:1`) (magical, reach 25 ft., unholy, versatile s), **Damage** 3d10+23 piercing"
  - name: "Melee strike"
    desc: "Jaws +34 (`pf2:1`) (magical, reach 15 ft., unarmed, unholy), **Damage** 4d6+20 piercing plus [[Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30<br>**9th** [[Falling Stars]], [[Massacre]]<br>**7th** [[Spell Riposte]]<br>**6th** [[Disintegrate]], [[Truesight]] (Constant)<br>**5th** [[Toxic Cloud]]<br>**4th** [[Translocate]], [[Translocate]]<br>**3rd** [[Paralyze]]"
abilities_bot:
  - name: "Consume Soul"
    desc: "`pf2:2` The obcisidaemon consumes a soul from their cloak to gain one of the following effects. A soul consumed in this way can't be resurrected except by a wish ritual or a similarly powerful effect. <br>  <br> *Empower Spell* The obcisidaemon gains a +2 status bonus to their spell DCs and spell attack modifiers until the end of their next turn. <br>  <br> *Empower Weapon* The obcisidaemon's weapon gains the effects of a greater flaming, greater frost, greater shock, or wounding rune until the end of their next turn. <br>  <br> *Healing* (healing, vitality) The daemon regains 8d8+64 healing Hit Points. <br>  <br> > [!danger] Effect: Consume Soul"
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

While war can have many facets, obcisidaemons care only for the brutality and violence that conflict brings. These devastating daemons seek only to destroy, leaving rubble and ash in their wake. Reflecting the mortal desire to fully eradicate one's enemy, obcisidaemons never intentionally leave a soul behind in their war paths. They claim the souls of those they slaughter, adding them to a profane cloak that seeps from their bodies as a clinging mist. Souls added to the cloak are unable to travel into the afterlife, and most obcisidaemons can hold only a handful of these souls at a time. Whenever an obcisidaemon's cloak is overburdened or during times when the fiend needs greater power, they consume a soul and receive rejuvenation or the might they need to cause further destruction.

```statblock
creature: "Obcisidaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
