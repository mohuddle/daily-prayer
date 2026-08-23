#!/usr/bin/env python3
"""Write rotating Method heads and occasional addresses (1710 public domain)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "web" / "data"

HEADS = {
    "adoration": [
        ("1.1", "Address God with reverence and awe", "God is in heaven, and I upon earth: therefore let my words be few. I will take off my shoes, for the place is holy.", "Ecclesiastes 5:2; Exodus 3:5"),
        ("1.2", "Reverently adore God", "Thou art a Spirit, infinite, eternal, and unchangeable in thy being, wisdom, power, holiness, justice, goodness, and truth.", "John 4:24; Psalm 90:2"),
        ("1.3", "God’s eternality and omnipresence", "From everlasting to everlasting thou art God. Whither shall I go from thy spirit? or whither shall I flee from thy presence?", "Psalm 90:2; Psalm 139:7"),
        ("1.4", "Perfect knowledge and unsearchable wisdom", "Great is our Lord, and of great power: his understanding is infinite. O the depth of the riches both of the wisdom and knowledge of God!", "Psalm 147:5; Romans 11:33"),
        ("1.5", "Incontestable sovereignty and power", "The Lord hath prepared his throne in the heavens; and his kingdom ruleth over all. He doeth according to his will in the army of heaven.", "Psalm 103:19; Daniel 4:35"),
        ("1.6", "Purity and justice", "Thou art of purer eyes than to behold evil. Justice and judgment are the habitation of thy throne: mercy and truth shall go before thy face.", "Habakkuk 1:13; Psalm 89:14"),
        ("1.7", "Unchanging truth and greatness", "Thy word is true from the beginning. Jesus Christ the same yesterday, and to day, and for ever.", "Psalm 119:160; Hebrews 13:8"),
        ("1.8", "Heavenly splendor and glory", "Holy, holy, holy, is the Lord of hosts: the whole earth is full of his glory. Thou art clothed with honour and majesty.", "Isaiah 6:3; Psalm 104:1"),
        ("1.9", "Glory to God as Creator", "Thou, even thou, art Lord alone; thou hast made heaven, the heaven of heavens, with all their host, the earth, and all things that are therein.", "Nehemiah 9:6"),
        ("1.10", "Honor the triune God", "Baptizing them in the name of the Father, and of the Son, and of the Holy Ghost. The grace of the Lord Jesus Christ, and the love of God, and the communion of the Holy Ghost, be with me.", "Matthew 28:19; 2 Corinthians 13:14"),
        ("1.11", "Dependence and obligation", "In him I live, and move, and have my being. What shall I render unto the Lord for all his benefits toward me?", "Acts 17:28; Psalm 116:12"),
        ("1.12", "Own my relation to God", "I will be to you a Father, and ye shall be to me sons and daughters, saith the Lord Almighty. Behold, what manner of love the Father hath bestowed upon us.", "2 Corinthians 6:18; 1 John 3:1"),
        ("1.13", "The privilege of drawing near", "Having therefore, brethren, boldness to enter into the holiest by the blood of Jesus, let me draw near with a true heart in full assurance of faith.", "Hebrews 10:19, 22"),
        ("1.14", "Unworthiness to draw near", "I am not worthy of the least of all the mercies, and of all the truth, which thou hast shewed unto thy servant. God be merciful to me a sinner.", "Genesis 32:10; Luke 18:13"),
        ("1.15", "Desire of the heart for God", "Whom have I in heaven but thee? and there is none upon earth that I desire beside thee. My soul thirsteth for God, for the living God.", "Psalm 73:25; Psalm 42:2"),
        ("1.16", "Believing hope and confidence", "I will trust, and not be afraid: for the Lord JEHOVAH is my strength and my song. They that know thy name will put their trust in thee.", "Isaiah 12:2; Psalm 9:10"),
        ("1.17", "Entreat favorable acceptance", "Let the words of my mouth, and the meditation of my heart, be acceptable in thy sight, O Lord, my strength, and my redeemer.", "Psalm 19:14"),
        ("1.18", "The Spirit’s assistance, and God’s glory", "The Spirit also helpeth our infirmities: for we know not what we should pray for as we ought. Whether therefore I eat, or drink, or whatsoever I do, let me do all to the glory of God.", "Romans 8:26; 1 Corinthians 10:31"),
        ("1.19", "Rely on Jesus alone", "I am the way, the truth, and the life: no man cometh unto the Father, but by me. Accepted in the beloved.", "John 14:6; Ephesians 1:6"),
    ],
    "confession": [
        ("2.1", "Take hold of encouragement to confess", "If we confess our sins, he is faithful and just to forgive us our sins, and to cleanse us from all unrighteousness. Let us therefore come boldly unto the throne of grace.", "1 John 1:9; Hebrews 4:16"),
        ("2.2", "Bewail original corruption", "Behold, I was shapen in iniquity; and in sin did my mother conceive me. I know that in me (that is, in my flesh,) dwelleth no good thing.", "Psalm 51:5; Romans 7:18"),
        ("2.3", "Blind understanding and stubborn will", "The heart is deceitful above all things, and desperately wicked. I have gone astray like a lost sheep; seek thy servant.", "Jeremiah 17:9; Psalm 119:176"),
        ("2.4", "Vain thoughts and carnal affections", "How long shall thy vain thoughts lodge within thee? The carnal mind is enmity against God.", "Jeremiah 4:14; Romans 8:7"),
        ("2.5", "Corruption of my entire being", "From the sole of the foot even unto the head there is no soundness. O wretched man that I am! who shall deliver me from the body of this death?", "Isaiah 1:6; Romans 7:24"),
        ("2.6", "Sins of omission", "To him that knoweth to do good, and doeth it not, to him it is sin. We have left undone those things which we ought to have done.", "James 4:17"),
        ("2.7", "Actual transgressions, especially pride", "God resisteth the proud, but giveth grace unto the humble. Search me, O God, and know my heart: try me, and know my thoughts.", "James 4:6; Psalm 139:23"),
        ("2.8", "Anger, love of the world, love of the flesh", "Be ye angry, and sin not. Love not the world, neither the things that are in the world. They that are Christ’s have crucified the flesh.", "Ephesians 4:26; 1 John 2:15; Galatians 5:24"),
        ("2.9", "False security, fretfulness, impatience", "Fret not thyself because of evildoers. Rest in the Lord, and wait patiently for him.", "Psalm 37:1, 7"),
        ("2.10", "Lack of love for others", "He that loveth not his brother abideth in death. Let all bitterness, and wrath, and anger, and clamour, and evil speaking, be put away from me, with all malice.", "1 John 3:14; Ephesians 4:31"),
        ("2.11", "Sins of the tongue and spiritual sloth", "If any man among you seem to be religious, and bridleth not his tongue, this man’s religion is vain. Not slothful in business; fervent in spirit; serving the Lord.", "James 1:26; Romans 12:11"),
        ("2.12", "The sinfulness and foolishness of sin", "Fools make a mock at sin. The way of transgressors is hard.", "Proverbs 14:9; Proverbs 13:15"),
        ("2.13", "The unprofitableness and deceitfulness of sin", "What fruit had ye then in those things whereof ye are now ashamed? The wages of sin is death.", "Romans 6:21, 23"),
        ("2.14", "Sin affronts God and damages the soul", "Against thee, thee only, have I sinned, and done this evil in thy sight. He that sinneth against me wrongeth his own soul.", "Psalm 51:4; Proverbs 8:36"),
        ("2.15", "Sin in light of knowledge and profession", "To him that knoweth to do good, and doeth it not, to him it is sin. Why call ye me, Lord, Lord, and do not the things which I say?", "James 4:17; Luke 6:46"),
        ("2.16", "Sin in light of mercies and warnings", "Despisest thou the riches of his goodness and forbearance? Or despisest thou the riches of his goodness, not knowing that the goodness of God leadeth thee to repentance?", "Romans 2:4"),
        ("2.17", "Sin in light of corrections and vows", "I will pay thee my vows, which my lips have uttered. It is good for me that I have been afflicted; that I might learn thy statutes.", "Psalm 66:13–14; Psalm 119:71"),
        ("2.18", "The condemning nature of sin", "The soul that sinneth, it shall die. Cursed is every one that continueth not in all things which are written in the book of the law to do them.", "Ezekiel 18:4; Galatians 3:10"),
        ("2.19", "Glory to God for patience and willingness to be reconciled", "The Lord is merciful and gracious, slow to anger, and plenteous in mercy. God was in Christ, reconciling the world unto himself.", "Psalm 103:8; 2 Corinthians 5:19"),
        ("2.20", "Sorrow and shame for sin", "I abhor myself, and repent in dust and ashes. A broken and a contrite heart, O God, thou wilt not despise.", "Job 42:6; Psalm 51:17"),
    ],
    "petition": [
        ("3.1", "Earnestly pray for forgiveness", "Have mercy upon me, O God, according to thy lovingkindness: according unto the multitude of thy tender mercies blot out my transgressions.", "Psalm 51:1"),
        ("3.2", "Plead God’s goodness and readiness to forgive", "Thou, Lord, art good, and ready to forgive; and plenteous in mercy unto all them that call upon thee.", "Psalm 86:5"),
        ("3.3", "Plead the merit and righteousness of Christ", "He hath made him to be sin for us, who knew no sin; that we might be made the righteousness of God in him.", "2 Corinthians 5:21"),
        ("3.4", "Plead the promises of pardon", "I, even I, am he that blotteth out thy transgressions for mine own sake, and will not remember thy sins.", "Isaiah 43:25"),
        ("3.5", "Plead my misery, and the blessedness of the pardoned", "Blessed is he whose transgression is forgiven, whose sin is covered. Heal me, O Lord, for my bones are vexed.", "Psalm 32:1; Psalm 6:2"),
        ("3.6", "Reconciliation and peace", "Being justified by faith, we have peace with God through our Lord Jesus Christ. Let the peace of God rule in my heart.", "Romans 5:1; Colossians 3:15"),
        ("3.7", "Covenant with God and knowledge of his favor", "I will be their God, and they shall be my people. Lord, lift thou up the light of thy countenance upon me.", "Jeremiah 31:33; Psalm 4:6"),
        ("3.8", "Blessing and abiding presence", "My presence shall go with thee, and I will give thee rest. The Lord bless thee, and keep thee.", "Exodus 33:14; Numbers 6:24"),
        ("3.9", "A sense of assurance", "The Spirit itself beareth witness with our spirit, that we are the children of God. Give me the earnest of the Spirit in my heart.", "Romans 8:16; 2 Corinthians 1:22"),
        ("3.10", "A well-grounded peace of conscience", "Let us draw near with a true heart in full assurance of faith, having our hearts sprinkled from an evil conscience.", "Hebrews 10:22"),
        ("3.11", "Grace to fortify me against everything evil", "Deliver us from evil. I pray God your whole spirit and soul and body be preserved blameless.", "Matthew 6:13; 1 Thessalonians 5:23"),
        ("3.12", "Grace against Satan’s temptations", "Put on the whole armour of God, that ye may be able to stand against the wiles of the devil. Resist the devil, and he will flee from you.", "Ephesians 6:11; James 4:7"),
        ("3.13", "Grace for everything good, and new life", "Make you perfect in every good work to do his will, working in you that which is wellpleasing in his sight. Create in me a clean heart, O God.", "Hebrews 13:21; Psalm 51:10"),
        ("3.14", "Grace to instruct me in the things of God", "Teach me thy way, O Lord; I will walk in thy truth. Open thou mine eyes, that I may behold wondrous things out of thy law.", "Psalm 86:11; Psalm 119:18"),
        ("3.15", "Grace to keep me in the way of truth", "Lead me in thy truth, and teach me. Buy the truth, and sell it not.", "Psalm 25:5; Proverbs 23:23"),
        ("3.16", "Grace to bring truth to my memory", "The Comforter, which is the Holy Ghost, shall teach you all things, and bring all things to your remembrance.", "John 14:26"),
        ("3.17", "A directed conscience, and wisdom", "If any of you lack wisdom, let him ask of God, that giveth to all men liberally. The entrance of thy words giveth light.", "James 1:5; Psalm 119:130"),
        ("3.18", "Grace to sanctify my nature", "Sanctify them through thy truth: thy word is truth. The very God of peace sanctify me wholly.", "John 17:17; 1 Thessalonians 5:23"),
        ("3.19", "Faith", "Lord, I believe; help thou mine unbelief. Without faith it is impossible to please him.", "Mark 9:24; Hebrews 11:6"),
        ("3.20", "The fear of God, and the love of God", "Unite my heart to fear thy name. Thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy mind.", "Psalm 86:11; Matthew 22:37"),
        ("3.21", "A tender conscience, and God-wrought love", "I will put my law in their inward parts, and write it in their hearts. The love of God is shed abroad in our hearts by the Holy Ghost.", "Jeremiah 31:33; Romans 5:5"),
        ("3.22", "Self-denial and humility", "If any man will come after me, let him deny himself. Be clothed with humility: for God resisteth the proud.", "Matthew 16:24; 1 Peter 5:5"),
        ("3.23", "Contentment and patience", "I have learned, in whatsoever state I am, therewith to be content. Let patience have her perfect work.", "Philippians 4:11; James 1:4"),
        ("3.24", "The grace of hope", "Now the God of hope fill you with all joy and peace in believing. Which hope we have as an anchor of the soul.", "Romans 15:13; Hebrews 6:19"),
        ("3.25", "Grace to preserve me from sin", "Hold thou me up, and I shall be safe. Keep back thy servant also from presumptuous sins.", "Psalm 119:117; Psalm 19:13"),
        ("3.26", "Grace to govern my tongue", "Set a watch, O Lord, before my mouth; keep the door of my lips. Let no corrupt communication proceed out of my mouth.", "Psalm 141:3; Ephesians 4:29"),
        ("3.27", "Walk wisely", "See then that ye walk circumspectly, not as fools, but as wise. So teach us to number our days, that we may apply our hearts unto wisdom.", "Ephesians 5:15; Psalm 90:12"),
        ("3.28", "Be honest in my duty", "Provide things honest in the sight of all men. Let your conversation be as it becometh the gospel of Christ.", "Romans 12:17; Philippians 1:27"),
        ("3.29", "Be diligent in my duty", "Not slothful in business; fervent in spirit; serving the Lord. Whatsoever thy hand findeth to do, do it with thy might.", "Romans 12:11; Ecclesiastes 9:10"),
        ("3.30", "Be courageous in my duty", "Be strong and of a good courage. Watch ye, stand fast in the faith, quit you like men, be strong.", "Joshua 1:9; 1 Corinthians 16:13"),
        ("3.31", "Be cheerful in my duty", "Rejoice in the Lord alway: and again I say, Rejoice. Serve the Lord with gladness.", "Philippians 4:4; Psalm 100:2"),
        ("3.32", "Do my duty always and everywhere", "Whether therefore ye eat, or drink, or whatsoever ye do, do all to the glory of God. In all thy ways acknowledge him.", "1 Corinthians 10:31; Proverbs 3:6"),
        ("3.33", "Be universally conscientious", "Then shall I not be ashamed, when I have respect unto all thy commandments. Herein do I exercise myself, to have always a conscience void of offence.", "Psalm 119:6; Acts 24:16"),
        ("3.34", "Wiser and better every day", "The path of the just is as the shining light, that shineth more and more unto the perfect day. Grow in grace, and in the knowledge of our Lord.", "Proverbs 4:18; 2 Peter 3:18"),
        ("3.35", "Support and comfort in afflictions", "This is my comfort in my affliction: for thy word hath quickened me. God is our refuge and strength, a very present help in trouble.", "Psalm 119:50; Psalm 46:1"),
        ("3.36", "Preserving grace", "Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ. Keep me as the apple of the eye.", "Philippians 1:6; Psalm 17:8"),
        ("3.37", "Grace to die well", "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me. Into thine hand I commit my spirit.", "Psalm 23:4; Psalm 31:5"),
        ("3.38", "Grace to fit me for heaven", "Father, I will that they also, whom thou hast given me, be with me where I am. We shall be like him; for we shall see him as he is.", "John 17:24; 1 John 3:2"),
        ("3.39", "Good things of life, and preservation in calamities", "Give us this day our daily bread. Thou shalt not be afraid for the terror by night; nor for the arrow that flieth by day.", "Matthew 6:11; Psalm 91:5"),
        ("3.40", "Daily supplies of comfort and support", "My God shall supply all your need according to his riches in glory by Christ Jesus. Having food and raiment let us be therewith content.", "Philippians 4:19; 1 Timothy 6:8"),
        ("3.41", "Plead the promises of God", "For all the promises of God in him are yea, and in him Amen. Put me in remembrance: let us plead together.", "2 Corinthians 1:20; Isaiah 43:26"),
    ],
    "thanksgiving": [
        ("4.1", "Stir myself up to praise, and thank him for his good nature", "It is a good thing to give thanks unto the Lord. The Lord is gracious, and full of compassion; slow to anger, and of great mercy.", "Psalm 92:1; Psalm 145:8"),
        ("4.2", "Thank God for kind providence", "O give thanks unto the Lord; for he is good: for his mercy endureth for ever. The earth is full of the goodness of the Lord.", "Psalm 136:1; Psalm 33:5"),
        ("4.3", "Thank God for his goodness continued", "Thou openest thine hand, and satisfiest the desire of every living thing. The eyes of all wait upon thee.", "Psalm 145:16, 15"),
        ("4.4", "Thank God for making me in his image", "I will praise thee; for I am fearfully and wonderfully made. God created man in his own image.", "Psalm 139:14; Genesis 1:27"),
        ("4.5", "Thank God for preserving me", "I laid me down and slept; I awaked; for the Lord sustained me. He hath holden me up from my birth.", "Psalm 3:5; Psalm 71:6"),
        ("4.6", "Thank God for recovery from danger", "Bless the Lord, O my soul, and forget not all his benefits: who forgiveth all thine iniquities; who healeth all thy diseases.", "Psalm 103:2–3"),
        ("4.7", "Supports and comforts of this life", "The lines are fallen unto me in pleasant places; yea, I have a goodly heritage. My cup runneth over.", "Psalm 16:6; Psalm 23:5"),
        ("4.8", "Successes and good relationships", "Except the Lord build the house, they labour in vain that build it. Behold, how good and how pleasant it is for brethren to dwell together in unity!", "Psalm 127:1; Psalm 133:1"),
        ("4.9", "The measure of peace I experience", "He maketh peace in thy borders. Pray for the peace of Jerusalem: they shall prosper that love thee.", "Psalm 147:14; Psalm 122:6"),
        ("4.10", "Grace to my soul, and the design of redemption", "God so loved the world, that he gave his only begotten Son. Thanks be unto God for his unspeakable gift.", "John 3:16; 2 Corinthians 9:15"),
        ("4.11", "Eternal purposes concerning redemption", "He hath chosen us in him before the foundation of the world. Known unto God are all his works from the beginning of the world.", "Ephesians 1:4; Acts 15:18"),
        ("4.12", "The appointing of the Redeemer", "When the fulness of the time was come, God sent forth his Son. Behold the Lamb of God, which taketh away the sin of the world.", "Galatians 4:4; John 1:29"),
        ("4.13", "Early indications of his gracious design", "The seed of the woman shall bruise the serpent’s head. Abraham rejoiced to see my day: and he saw it, and was glad.", "Genesis 3:15; John 8:56"),
        ("4.14", "Favor to the Old Testament church", "Unto them were committed the oracles of God. The Lord of hosts is with us; the God of Jacob is our refuge.", "Romans 3:2; Psalm 46:7"),
        ("4.15", "The incarnation of the Son of God", "The Word was made flesh, and dwelt among us. Unto you is born this day in the city of David a Saviour, which is Christ the Lord.", "John 1:14; Luke 2:11"),
        ("4.16", "The Father’s owning of Christ", "This is my beloved Son, in whom I am well pleased. God anointed Jesus of Nazareth with the Holy Ghost and with power.", "Matthew 3:17; Acts 10:38"),
        ("4.17", "Christ’s holy life, doctrine, and miracles", "He went about doing good. Never man spake like this man.", "Acts 10:38; John 7:46"),
        ("4.18", "Encouragement to poor sinners to come", "Come unto me, all ye that labour and are heavy laden, and I will give you rest. Him that cometh to me I will in no wise cast out.", "Matthew 11:28; John 6:37"),
        ("4.19", "The cross of Christ and its benefits", "God forbid that I should glory, save in the cross of our Lord Jesus Christ. The blood of Jesus Christ his Son cleanseth us from all sin.", "Galatians 6:14; 1 John 1:7"),
        ("4.20", "The purchases and triumphs of the cross", "Who his own self bare our sins in his own body on the tree. Having spoiled principalities and powers, he made a shew of them openly.", "1 Peter 2:24; Colossians 2:15"),
        ("4.21", "Christ’s resurrection", "The Lord is risen indeed. He was delivered for our offences, and was raised again for our justification.", "Luke 24:34; Romans 4:25"),
        ("4.22", "Christ’s ascension", "Thou hast ascended on high, thou hast led captivity captive. I go to prepare a place for you.", "Psalm 68:18; John 14:2"),
        ("4.23", "Christ’s intercession", "He ever liveth to make intercession for them. We have an advocate with the Father, Jesus Christ the righteous.", "Hebrews 7:25; 1 John 2:1"),
        ("4.24", "The Redeemer’s dominion", "All power is given unto me in heaven and in earth. He must reign, till he hath put all enemies under his feet.", "Matthew 28:18; 1 Corinthians 15:25"),
        ("4.25", "Assurance of his second coming", "This same Jesus, which is taken up from you into heaven, shall so come in like manner. Even so, come, Lord Jesus.", "Acts 1:11; Revelation 22:20"),
        ("4.26", "The sending of the Holy Spirit", "I will pray the Father, and he shall give you another Comforter. The Spirit of truth will guide you into all truth.", "John 14:16; John 16:13"),
        ("4.27", "The covenant of grace", "I will be to them a God, and they shall be to me a people. This is my blood of the new testament, which is shed for many for the remission of sins.", "Hebrews 8:10; Matthew 26:28"),
        ("4.28", "The Scriptures", "All scripture is given by inspiration of God. Thy word is a lamp unto my feet, and a light unto my path.", "2 Timothy 3:16; Psalm 119:105"),
        ("4.29", "The ministry and other ordinances", "He gave some, apostles; and some, prophets; and some, evangelists; and some, pastors and teachers. Not forsaking the assembling of ourselves together.", "Ephesians 4:11; Hebrews 10:25"),
        ("4.30", "The planting of the church", "I will build my church; and the gates of hell shall not prevail against it. The Lord added to the church daily such as should be saved.", "Matthew 16:18; Acts 2:47"),
        ("4.31", "The preservation of Christianity", "Upon this rock I will build my church. He that keepeth Israel shall neither slumber nor sleep.", "Matthew 16:18; Psalm 121:4"),
        ("4.32", "Martyrs and confessors", "These all died in faith. Be thou faithful unto death, and I will give thee a crown of life.", "Hebrews 11:13; Revelation 2:10"),
        ("4.33", "The communion of saints", "We, being many, are one body in Christ. If we walk in the light, we have fellowship one with another.", "Romans 12:5; 1 John 1:7"),
        ("4.34", "The hope of eternal life", "Blessed be the God and Father of our Lord Jesus Christ, which according to his abundant mercy hath begotten us again unto a lively hope.", "1 Peter 1:3"),
        ("4.35", "Every Spirit-wrought inward change", "If any man be in Christ, he is a new creature. A new heart also will I give you, and a new spirit will I put within you.", "2 Corinthians 5:17; Ezekiel 36:26"),
        ("4.36", "Remission of sins and peace of conscience", "In whom we have redemption through his blood, the forgiveness of sins. Being justified by faith, we have peace with God.", "Ephesians 1:7; Romans 5:1"),
        ("4.37", "Powerful influences of divine grace", "It is God which worketh in you both to will and to do of his good pleasure. My grace is sufficient for thee.", "Philippians 2:13; 2 Corinthians 12:9"),
        ("4.38", "Sweet communion in holy ordinances", "One thing have I desired of the Lord, that will I seek after; that I may dwell in the house of the Lord all the days of my life.", "Psalm 27:4"),
        ("4.39", "Gracious answers to prayer", "I love the Lord, because he hath heard my voice and my supplications. Ask, and ye shall receive, that your joy may be full.", "Psalm 116:1; John 16:24"),
        ("4.40", "Support under afflictions", "It is good for me that I have been afflicted. Our light affliction, which is but for a moment, worketh for us a far more exceeding and eternal weight of glory.", "Psalm 119:71; 2 Corinthians 4:17"),
        ("4.41", "The performance of his promises", "There hath not failed one word of all his good promise. He is faithful that promised.", "1 Kings 8:56; Hebrews 10:23"),
    ],
    "intercession": [
        ("5.1", "Propagation of the gospel", "Pray ye therefore the Lord of the harvest, that he will send forth labourers into his harvest. That thy way may be known upon earth, thy saving health among all nations.", "Matthew 9:38; Psalm 67:2"),
        ("5.2", "The ancient people of God, and churches in hard places", "My heart’s desire and prayer to God for Israel is, that they might be saved. Look upon Zion, the city of our solemnities.", "Romans 10:1; Isaiah 33:20"),
        ("5.3", "The universal church", "Peace be within thy walls, and prosperity within thy palaces. Upon this rock I will build my church.", "Psalm 122:7; Matthew 16:18"),
        ("5.4", "Conversion of those hostile to the faith", "God our Saviour will have all men to be saved, and to come unto the knowledge of the truth. Who will have all men to be saved.", "1 Timothy 2:3–4"),
        ("5.5", "Health, purity, and holiness of the church", "Christ also loved the church, and gave himself for it; that he might sanctify and cleanse it. That he might present it to himself a glorious church.", "Ephesians 5:25–27"),
        ("5.6", "That the gospel would not be overthrown", "Upon this rock I will build my church; and the gates of hell shall not prevail against it. No weapon that is formed against thee shall prosper.", "Matthew 16:18; Isaiah 54:17"),
        ("5.7", "Suffering churches and the persecuted", "Remember them that are in bonds, as bound with them; and them which suffer adversity. If one member suffer, all the members suffer with it.", "Hebrews 13:3; 1 Corinthians 12:26"),
        ("5.8", "The nations, and my own nation", "The kingdoms of this world are become the kingdoms of our Lord. Seek the peace of the city.", "Revelation 11:15; Jeremiah 29:7"),
        ("5.9", "National mercies and the gospel ministry", "I will give you pastors according to mine heart, which shall feed you with knowledge and understanding. Let thy priests be clothed with righteousness.", "Jeremiah 3:15; Psalm 132:9"),
        ("5.10", "Outward peace and tranquillity", "He maketh peace in thy borders. Pray for kings, and for all that are in authority; that we may lead a quiet and peaceable life.", "Psalm 147:14; 1 Timothy 2:2"),
        ("5.11", "Moral decency and civility", "Righteousness exalteth a nation: but sin is a reproach to any people. He that ruleth over men must be just, ruling in the fear of God.", "Proverbs 14:34; 2 Samuel 23:3"),
        ("5.12", "Healing of unhappy divisions", "Endeavouring to keep the unity of the Spirit in the bond of peace. Behold, how good and how pleasant it is for brethren to dwell together in unity!", "Ephesians 4:3; Psalm 133:1"),
        ("5.13", "Those who govern", "I exhort that prayers be made for kings, and for all that are in authority. The king’s heart is in the hand of the Lord.", "1 Timothy 2:1–2; Proverbs 21:1"),
        ("5.14", "Civil government", "Let every soul be subject unto the higher powers. For there is no power but of God. The powers that be are ordained of God.", "Romans 13:1"),
        ("5.15", "Those employed in public affairs", "He that ruleth over men must be just. Wisdom and knowledge shall be the stability of thy times.", "2 Samuel 23:3; Isaiah 33:6"),
        ("5.16", "Judges and judicial rulers", "Defend the poor and fatherless: do justice to the afflicted and needy. He hath shewed thee, O man, what is good; and what doth the Lord require of thee, but to do justly.", "Psalm 82:3; Micah 6:8"),
        ("5.17", "Ministers of the word and sacraments", "Pray for us, that the word of the Lord may have free course. And for me, that utterance may be given unto me, that I may open my mouth boldly.", "2 Thessalonians 3:1; Ephesians 6:19"),
        ("5.18", "Schools and common citizens", "The fear of the Lord is the beginning of knowledge. That we may lead a quiet and peaceable life in all godliness and honesty.", "Proverbs 1:7; 1 Timothy 2:2"),
        ("5.19", "The young and the old", "Even the youths shall faint and be weary. Those that be planted in the house of the Lord shall flourish in the courts of our God. They shall still bring forth fruit in old age.", "Isaiah 40:30; Psalm 92:13–14"),
        ("5.20", "Rich and poor, enemies and friends", "The rich and poor meet together: the Lord is the maker of them all. Love your enemies, bless them that curse you, do good to them that hate you, and pray for them which despitefully use you.", "Proverbs 22:2; Matthew 5:44"),
    ],
    "conclusion": [
        ("6.1", "Acceptance of my prayers for Christ’s sake", "Whatsoever ye shall ask the Father in my name, he will give it you. Let my prayer be set forth before thee as incense.", "John 16:23; Psalm 141:2"),
        ("6.2", "Forgiveness for what has been amiss in prayer", "We know not what we should pray for as we ought. If I regard iniquity in my heart, the Lord will not hear me: yet he is merciful.", "Romans 8:26; Psalm 66:18"),
        ("6.3", "Commend myself to the grace of God", "I commend you to God, and to the word of his grace. My grace is sufficient for thee.", "Acts 20:32; 2 Corinthians 12:9"),
        ("6.4", "Solemn praises of God", "Blessing, and glory, and wisdom, and thanksgiving, and honour, and power, and might, be unto our God for ever and ever. Amen.", "Revelation 7:12"),
        ("6.5", "Sum up with the Lord’s Prayer", "After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name.", "Matthew 6:9"),
    ],
}

OCCASIONAL = [
    {
        "id": "8.1",
        "title": "If this is morning",
        "when": ["morning"],
        "prayers": [
            {"text": "O God, thou art my God; early will I seek thee. Cause me to hear thy lovingkindness in the morning; for in thee do I trust.", "ref": "Psalm 63:1; Psalm 143:8"},
            {"text": "It is of the Lord’s mercies that I am not consumed, because his compassions fail not. They are new every morning.", "ref": "Lamentations 3:22–23"},
            {"text": "Let the beauty of the Lord our God be upon me: and establish thou the work of my hands upon me.", "ref": "Psalm 90:17"},
        ],
    },
    {
        "id": "8.2",
        "title": "If this is evening",
        "when": ["evening"],
        "prayers": [
            {"text": "I will both lay me down in peace, and sleep: for thou, Lord, only makest me dwell in safety.", "ref": "Psalm 4:8"},
            {"text": "Let my prayer be set forth before thee as incense; and the lifting up of my hands as the evening sacrifice.", "ref": "Psalm 141:2"},
            {"text": "Into thine hand I commit my spirit: thou hast redeemed me, O Lord God of truth.", "ref": "Psalm 31:5"},
        ],
    },
    {
        "id": "8.6",
        "title": "Evening before the Lord’s Day",
        "when": ["saturday"],
        "prayers": [
            {"text": "Remember the sabbath day, to keep it holy. I was glad when they said unto me, Let us go into the house of the Lord.", "ref": "Exodus 20:8; Psalm 122:1"},
            {"text": "Prepare to meet thy God. Let me lay aside this world’s cares, and call the sabbath a delight.", "ref": "Amos 4:12; Isaiah 58:13"},
        ],
    },
    {
        "id": "8.7",
        "title": "Morning of the Lord’s Day",
        "when": ["sunday"],
        "prayers": [
            {"text": "This is the day which the Lord hath made; we will rejoice and be glad in it. I was in the Spirit on the Lord’s day.", "ref": "Psalm 118:24; Revelation 1:10"},
            {"text": "How amiable are thy tabernacles, O Lord of hosts! My soul longeth, yea, even fainteth for the courts of the Lord.", "ref": "Psalm 84:1–2"},
        ],
    },
    {
        "id": "8.8",
        "title": "Public worship",
        "when": ["sunday"],
        "prayers": [
            {"text": "Not forsaking the assembling of ourselves together. Let us go into the house of the Lord.", "ref": "Hebrews 10:25; Psalm 122:1"},
            {"text": "The Lord is in his holy temple: let all the earth keep silence before him. Let the word of Christ dwell in me richly.", "ref": "Habakkuk 2:20; Colossians 3:16"},
        ],
    },
    {
        "id": "8.3",
        "title": "Before a meal",
        "when": [],
        "prayers": [
            {"text": "Every creature of God is good, and nothing to be refused, if it be received with thanksgiving: for it is sanctified by the word of God and prayer.", "ref": "1 Timothy 4:4–5"},
            {"text": "Give us this day our daily bread. Whether therefore ye eat, or drink, or whatsoever ye do, do all to the glory of God.", "ref": "Matthew 6:11; 1 Corinthians 10:31"},
        ],
    },
    {
        "id": "8.4",
        "title": "After a meal",
        "when": [],
        "prayers": [
            {"text": "When thou hast eaten and art full, then thou shalt bless the Lord thy God. Bless the Lord, O my soul, and forget not all his benefits.", "ref": "Deuteronomy 8:10; Psalm 103:2"},
        ],
    },
    {
        "id": "8.5",
        "title": "For travelling",
        "when": [],
        "prayers": [
            {"text": "The Lord shall preserve thy going out and thy coming in from this time forth, and even for evermore.", "ref": "Psalm 121:8"},
            {"text": "In all thy ways acknowledge him, and he shall direct thy paths.", "ref": "Proverbs 3:6"},
        ],
    },
    {
        "id": "8.15",
        "title": "For one weighed down",
        "when": [],
        "prayers": [
            {"text": "Come unto me, all ye that labour and are heavy laden, and I will give you rest. Cast thy burden upon the Lord, and he shall sustain thee.", "ref": "Matthew 11:28; Psalm 55:22"},
            {"text": "Bear ye one another’s burdens, and so fulfil the law of Christ.", "ref": "Galatians 6:2"},
        ],
    },
    {
        "id": "8.17",
        "title": "For the sick and weak",
        "when": [],
        "prayers": [
            {"text": "Is any sick among you? let him call for the elders of the church. The prayer of faith shall save the sick.", "ref": "James 5:14–15"},
            {"text": "Himself took our infirmities, and bare our sicknesses. Heal me, O Lord, and I shall be healed.", "ref": "Matthew 8:17; Jeremiah 17:14"},
        ],
    },
]


def pack_heads() -> dict:
    out = {}
    for section, rows in HEADS.items():
        out[section] = [
            {"id": hid, "title": title, "pray": pray, "ref": ref}
            for hid, title, pray, ref in rows
        ]
    return out


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    heads = {
        "meta": {
            "source": "Matthew Henry, A Method for Prayer (1710). Public domain.",
            "note": "One head from each chapter is appointed by day of year, cycling the index.",
        },
        "sections": pack_heads(),
    }
    occasional = {
        "meta": {
            "source": "Matthew Henry, A Method for Prayer (1710), occasional addresses.",
            "note": "Lord’s Day items surface on Saturday and Sunday. Morning and evening follow the clock. The rest wait in the drawer.",
        },
        "items": OCCASIONAL,
    }
    (DATA / "heads.json").write_text(json.dumps(heads, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "occasional.json").write_text(json.dumps(occasional, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = {k: len(v) for k, v in heads["sections"].items()}
    print("heads", counts, "occasional", len(OCCASIONAL))


if __name__ == "__main__":
    main()
