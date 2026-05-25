---
type: creature
group: ["Dragon", "Occult"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Conspirator Dragon (Adult, Spellcaster)"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Shadowtongue, Sussuran (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +21, Athletics +23, Deception +25, Diplomacy +25, Intimidation +23, Occultism +23, Performance +25, Society +23, Stealth +21, Lore (any one region or settlement) +25"
abilityMods: ["+5", "+3", "+4", "+5", "+5", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Conjure Disguise"
    desc: "**Frequency** once per day <br>  <br> **Effect** The dragon conjures a perfect flesh-suit replica of a humanoid they've seen of their size or smaller and compresses themself into it, along with generating appropriate clothing for the humanoid. This process takes 1 minute to complete, during which the dragon is [[Off Guard]]. If the dragon stops or is interrupted in this process, the suit is destroyed. Once the process is complete, the dragon can remain in this disguise indefinitely. <br>  <br> The transformation has the effects of [[Change Shape]], except that the disguise is not actively magical in nature and doesn't register as magical to detect magic and similar effects. The dragon loses Retract Body while transformed. <br>  <br> If the dragon is critically hit while wearing the disguise, the suit is destroyed and immediately explodes. This has the effects of Detonate Disguise, except that creatures use the outcome one degree of success better than they rolled on their save."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 2d6 precision damage to [[Off Guard]] targets."
armorclass:
  - name: AC
    desc: "33; **Fort** +20, **Ref** +21, **Will** +25"
health:
  - name: HP
    desc: "215; **Immunities** controlled, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Occult"
    desc: ""
  - name: "Retract Body"
    desc: "`pf2:r` **Trigger** The dragon is hit or critically hit by an attack made by a creature the dragon can see <br>  <br> **Effect** The dragon retracts the targeted body part or twists away to avoid the attack, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +25 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d8+11 piercing"
  - name: "Melee strike"
    desc: "Claw +25 (`pf2:1`) (agile, magical, unarmed), **Damage** 3d6+11 slashing"
  - name: "Melee strike"
    desc: "Tail +23 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d10+11 bludgeoning"
  - name: "Ranged strike"
    desc: "Mental Blast +25 (`pf2:1`) (mental), **Damage** 3d6+6 mental"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 33, attack +25<br>**5th** (3 slots) [[Scouting Eye]], [[Synaptic Pulse]], [[Truespeech]]<br>**4th** (3 slots) [[Clairvoyance]], [[Honeyed Words]], [[Suggestion]]<br>**3rd** (3 slots) [[Clairaudience]], [[Paralyze]], [[Veil of Privacy]]<br>**2nd** (3 slots) [[Calm]], [[Invisibility]], [[Paranoia]]<br>**1st** (3 slots) [[Bane]], [[Fear]], [[Phantom Pain]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Figment]], [[Message]], [[Telekinetic Projectile]]"
  - name: "Occult Innate Spells"
    desc: "DC 32, attack +24<br>**5th** [[Mind Probe]]<br>**4th** [[Rewrite Memory]]<br>**3rd** [[Mind Reading]] (At Will)<br>**1st** [[Charm]], [[Charm]] (At Will)"
abilities_bot:
  - name: "Detonate Disguise"
    desc: "`pf2:2` **Requirements** The dragon is wearing their conjured disguise <br>  <br> **Effect** The dragon erupts from the disguise, destroying it. The explosive revelation deals @Damage[13d6[bludgeoning]|options:area-damage] damage to creatures in a @Template[emanation|distance:5] with a DC 31 [[Reflex]] save. A creature that fails its save is [[Dazzled]] for 1 round as it becomes covered in scraps from the disguise. <br>  <br> Any creature sharing a space with the dragon after they erupt is pushed into the nearest empty space."
  - name: "Rushed Transformation"
    desc: "`pf2:3` **Frequency** once per hour <br>  <br> **Effect** Using the aid of magic and an exhausting amount of effort, the dragon quickly reshapes their body into the form of a generic humanoid figure. This has the effects of [[Humanoid Form]] except that it lasts only 1 minute, and the dragon doesn't gain the +4 status bonus to Deception as the transformation makes use of the dragon's body to crudely mimic a humanoid form. The dragon can Dismiss the effect. <br>  <br> Whenever the effect ends, the dragon leaves behind scraps of magically conjured flesh, which could give away the dragon's presence."
  - name: "Smoke Breath"
    desc: "`pf2:2` The dragon unleashes a noxious cloud of smoke that deals @Damage[10d6[poison]|options:area-damage] damage in a @Template[cone|distance:50] (DC 33 [[Fortitude]] save). The smoke remains for 1 minute. This has the effects of [[Mist]], except it fills the cone's area. <br>  <br> The dragon can't use Smoke Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hidden among the shadows and upper echelons of society are the conspirator dragons. These dragons are schemers, always looking to manipulate and control others, either for personal gain or simply for the thrill of watching their machinations play out. Conspirator dragons see themselves above others and typically speak with infantilizing tones and words. However, as most conspirator dragons meet others while in disguise, they do their best to maintain their disguise.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Conspirator Dragon (Adult, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
