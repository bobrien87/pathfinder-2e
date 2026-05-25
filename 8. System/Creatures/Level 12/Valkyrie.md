---
type: creature
group: ["Aesir", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Valkyrie"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aesir"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Common, Jotun (ravenspeaker, truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +25, Diplomacy +23, Intimidation +23, Religion +22"
abilityMods: ["+7", "+5", "+5", "+3", "+4", "+5"]
abilities_top:
  - name: "Claimer of the Slain"
    desc: "Valkyries can detect the souls of those recently slain in combat. A valkyrie spends 10 minutes praying over the body of a creature who has been dead for no more than 12 hours; if that creature is worthy of becoming an Einherji, the valkyrie transforms that creature into an einherji."
  - name: "Ravenspeaker"
    desc: "Valkyries use ravens as servants and spies. They can speak with ravens, and they can have up to three raven servitors who follow their commands. Valkyries can constantly observe whatever their commanded ravens sense."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "33; **Fort** +24, **Ref** +20, **Will** +23"
health:
  - name: HP
    desc: "215; **Resistances** electricity 15"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within your reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> You lash out at a foe that leaves an opening. Make a melee Strike against the triggering creature. If your attack is a critical hit and the trigger was a manipulate action, you disrupt that action. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike."
  - name: "Recall the Fallen"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** An allied creature within 60 feet who isn't a construct or undead is reduced to 0 Hit Points and their [[Dying]] value is 2 or less <br>  <br> **Effect** The valkyrie restores 5d10 healing Hit Points to the target."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +28 (`pf2:1`) (magical), **Damage** 2d6+15 piercing plus 1d12 electricity"
  - name: "Melee strike"
    desc: "Spear +26 (`pf2:1`) (magical, thrown 20), **Damage** 2d6+15 piercing plus 1d12 electricity"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**7th** [[Interplanar Teleport (self and mount only)]]<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Heroism]], [[Heroism]], [[Safe Passage]]<br>**2nd** [[Augury]], [[Status]]<br>**1st** [[Heal]], [[Infuse Vitality]]"
abilities_bot:
  - name: "Storm of Battle"
    desc: "`pf2:2` The valkyrie hurls her spear into the air, creating a massive storm in a @Template[burst|distance:100]. Spears of lightning rain down upon enemies in the area, dealing @Damage[4d12[electricity]|options:area-damage] damage (DC 32 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The song of the valkyries plays wherever steel rings against steel. Choosers of the slain and so-called angels of battle, valkyries are humanoid individuals of impressive physical stature who seek the most epic battles and legendary conficts so they can lay claim to the souls of the world's greatest warriors. The valkyries transform these souls into the implacable immortals known as einherjar.

Valkyries most often serve gods of battle and war, though one might pledge their service to any deity they consider worthy. Gorum was particularly well known for having valkyrie and einherjar servants. Besmara also has valkyrie servitors, and many stories of "ghost ships" actually reference accounts of encounters with ships crewed by einherjar devoted to the Pirate Queen.

```statblock
creature: "Valkyrie"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
